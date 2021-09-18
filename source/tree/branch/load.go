package branch

import (
	"io"
	"os"
	"fmt"

	"crypto/sha256"
	"encoding/hex"

	"log"
	"io/ioutil"
	"path/filepath"

	"github.com/inigo-selwood/barbican/tree/asset/header"
	"github.com/inigo-selwood/barbican/tree/asset/source"
)

func Load(name string, root string, parent *Branch) (*Branch, error) {
	branch := Branch{
		Name:      name,
		Hash:      "",
		RealRoute: "",
		HashRoute: "",
		Size:      0,
		Parent:    parent,
		Headers:   make(map[string]*header.Header),
		Sources:   make(map[string]*source.Source),
		Branches:  make(map[string]*Branch),
	}

	// Evaluate the branch path, route, and name
	var relativePath string
	if parent != nil {
		relativePath = filepath.Join(root, parent.RealRoute, name)
	} else {
		relativePath = filepath.Join(root, name)
	}

	branchPath, pathError := filepath.Abs(relativePath)
	if pathError != nil {
		return nil, pathError
	}

	var routeError error
	branch.RealRoute, routeError = filepath.Rel(root, branchPath)
	if routeError != nil {
		return nil, routeError
	}

	// Read entries in the branch
	entries, entriesError := ioutil.ReadDir(branchPath)
	if entriesError != nil {
		log.Fatal(entriesError)
	}

	// Handle headers, sources, and child branches
	var entryHashes []string
	for _, entry := range entries {
		entryName := entry.Name()

		// Create sub-branches
		if entry.Mode().IsDir() {
			if entryName == ".barbican" {
				continue
			}

			newBranch, branchError := Load(entryName,
					root,
					&branch)
			if branchError != nil {
				return nil, branchError
			}

			entryHashes = append(entryHashes, newBranch.Hash)
			branch.Size += newBranch.Size
			branch.Branches[entryName] = newBranch

		} else if entry.Mode().IsRegular() {
			assetExtension := filepath.Ext(entryName)

			// Process header files
			if assetExtension == ".hpp" {
				instance, headerError := header.Load(entryName,
						branch.RealRoute,
						root)
				if headerError != nil {
					return nil, headerError
				}

				entryHashes = append(entryHashes, instance.Hash)
				branch.Size += instance.Size
				branch.Headers[entryName] = instance

			// Process source files
			} else if assetExtension == ".cpp" {
				instance, sourceError := source.Load(entryName,
						branch.RealRoute,
						root)
				if sourceError != nil {
					return nil, sourceError
				}

				entryHashes = append(entryHashes, instance.Hash)
				branch.Size += instance.Size
				branch.Sources[entryName] = instance
			}
		}
	}

	// Create a hash from the entries in the branch
	hashContext := sha256.New()
	for _, entryHash := range entryHashes {
		io.WriteString(hashContext, entryHash)
	}
	branch.Hash = hex.EncodeToString(hashContext.Sum(nil))[:10]

	// Evaluate the new hashed route
	if parent != nil {
		branch.HashRoute = filepath.Join(parent.HashRoute, branch.Hash)
	} else {
		branch.HashRoute = branch.Hash
	}

	// Mark new/changed headers
	for _, headerInstance := range branch.Headers {
	    buildName := fmt.Sprintf("%s.o", headerInstance.Hash)
	    hashPath := filepath.Join(root, branch.HashRoute, buildName)

	    _, statusError := os.Stat(hashPath)
	    if os.IsNotExist(statusError) == true {
	        headerInstance.Dirty = true
	    }
	}

	// Mark new/changed sources
	for _, sourceInstance := range branch.Sources {
	    buildName := fmt.Sprintf("%s.o", sourceInstance.Hash)
	    hashPath := filepath.Join(root, branch.HashRoute, buildName)

	    _, statusError := os.Stat(hashPath)
	    if os.IsNotExist(statusError) == true {
	        sourceInstance.Dirty = true
	    }
	}

	return &branch, nil
}

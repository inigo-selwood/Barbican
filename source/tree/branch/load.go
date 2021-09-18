package branch

import (
	"io"

	"crypto/sha256"
	"encoding/hex"

	"log"
	"io/ioutil"
	"path/filepath"

	"github.com/inigo-selwood/barbican/tree/asset/header"
	"github.com/inigo-selwood/barbican/tree/asset/source"
)

func Load(name string,
		route string,
		root string,
		parent *Branch) (*Branch, error) {

	relativePath := filepath.Join(root, route, name)
	branchPath, pathError := filepath.Abs(relativePath)
	if pathError != nil {
		return nil, pathError
	}

	branchRoute, routeError := filepath.Rel(root, branchPath)
	if routeError != nil {
		return nil, routeError
	}

	entries, entriesError := ioutil.ReadDir(branchPath)
	if entriesError != nil {
		log.Fatal(entriesError)
	}

	branch := Branch{
		Name:     name,
		Hash:     "",
		Size:     0,
		Headers:  make(map[string]*header.Header),
		Sources:  make(map[string]*source.Source),
		Branches: make(map[string]*Branch),
	}

	var entryHashes []string
	for _, entry := range entries {
		entryName := entry.Name()

		if entry.Mode().IsDir() {
			newBranch, branchError := Load(entryName,
					branchRoute,
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
			if assetExtension == ".hpp" {
				instance, headerError := header.Load(entryName,
						branchRoute,
						root)
				if headerError != nil {
					return nil, headerError
				}

				entryHashes = append(entryHashes, instance.Hash)
				branch.Size += instance.Size
				branch.Headers[entryName] = instance
			} else if assetExtension == ".cpp" {
				instance, sourceError := source.Load(entryName,
						branchRoute,
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

	hashContext := sha256.New()
	for _, entryHash := range entryHashes {
		io.WriteString(hashContext, entryHash)
	}
	branch.Hash = hex.EncodeToString(hashContext.Sum(nil))[:10]

	return &branch, nil
}

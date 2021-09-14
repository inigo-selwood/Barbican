package branch

import (
	"log"
	"io/ioutil"
	"path/filepath"

	"github.com/inigo-selwood/barbican/tree/asset/header"
	"github.com/inigo-selwood/barbican/tree/asset/source"
)

func Load(name string, route string, root string) (*Branch, error) {
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

	var size int64 = 0
	branches := make(map[string]*Branch)
	headers := make(map[string]*header.Header)
	sources := make(map[string]*source.Source)
	for _, entry := range entries {
		entryName := entry.Name()

		if entry.Mode().IsDir() {
			newBranch, branchError := Load(entryName, branchRoute, root)
			if branchError != nil {
				return nil, branchError
			}

			size += newBranch.Size
			branches[entryName] = newBranch
		} else if entry.Mode().IsRegular() {

			assetExtension := filepath.Ext(entryName)
			if assetExtension == ".hpp" {
				instance, headerError := header.Load(entryName,
						branchRoute,
						root)
				if headerError != nil {
					return nil, headerError
				}

				size += instance.Size
				headers[entryName] = instance
			} else if assetExtension == ".cpp" {
				instance, sourceError := source.Load(entryName,
						branchRoute,
						root)
				if sourceError != nil {
					return nil, sourceError
				}

				size += instance.Size
				sources[entryName] = instance
			}
		}
	}

	branch := Branch{
		Name:     name,
		Size:     size,
		Headers:  headers,
		Sources:  sources,
		Branches: branches,
	}

	return &branch, nil
}

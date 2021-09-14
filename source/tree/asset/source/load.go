package source

import (
	"os"

	"path/filepath"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/asset"
)

func Load(name string, route string, root string) (*Source, error) {
	relativePath := filepath.Join(root, route, name)
	sourcePath, pathError := filepath.Abs(relativePath)
	if pathError != nil {
		return nil, pathError
	}

	sourceStatus, statusError := os.Lstat(sourcePath)
	if statusError != nil {
		return nil, statusError
	}

	headers := make(map[string]*asset.Asset)
	headerNames := tree.ReadHeaders(sourcePath)
	for _, headerName := range headerNames {
		headers[headerName] = nil
	}

	source := Source{
		Name:    name,
		Hash:    tree.DeepHashFile(sourcePath),
		Size:    sourceStatus.Size(),
		Headers: headers,
	}

	return &source, nil
}

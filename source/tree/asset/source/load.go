package source

import (
	"os"

	"path/filepath"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/asset"
)

func Load(name string, realRoute string, root string) (*Source, error) {

	// Evaluate absolute path
	relativePath := filepath.Join(root, realRoute, name)
	sourcePath, pathError := filepath.Abs(relativePath)
	if pathError != nil {
		return nil, pathError
	}

	// Read file status information
	sourceStatus, statusError := os.Lstat(sourcePath)
	if statusError != nil {
		return nil, statusError
	}

	// Add route keys for each header
	headers := make(map[string]asset.Asset)
	headerNames := tree.ReadHeaders(sourcePath)
	for _, headerName := range headerNames {
		headers[headerName] = nil
	}

	// Create and return source object
	source := Source{
		Name:    name,
		Hash:    tree.DeepHashFile(sourcePath),
		Size:    sourceStatus.Size(),
		Headers: headers,
	}
	return &source, nil
}

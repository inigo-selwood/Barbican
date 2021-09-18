package header

import (
	"os"

	"path/filepath"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/asset"
)

func Load(name string, realRoute string, root string) (*Header, error) {

	// Evaluate absolute path
	relativePath := filepath.Join(root, realRoute, name)
	headerPath, pathError := filepath.Abs(relativePath)
	if pathError != nil {
		return nil, pathError
	}

	// Read file status
	headerStatus, statusError := os.Lstat(headerPath)
	if statusError != nil {
		return nil, statusError
	}

	// Add keys for each header route
	headers := make(map[string]asset.Asset)
	headerNames := tree.ReadHeaders(headerPath)
	for _, headerName := range headerNames {
		headers[headerName] = nil
	}

	// Create and return header object
	header := Header{
		Name:    name,
		Hash:    tree.DeepHashFile(headerPath),
		Size:    headerStatus.Size(),
		Headers: headers,
		Sources: make(map[string]asset.Asset),
	}

	return &header, nil
}

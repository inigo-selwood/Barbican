package header

import (
	"os"

	"path/filepath"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/asset"
)

func Load(name string, route string, root string) (*Header, error) {
	relativePath := filepath.Join(root, route, name)
	headerPath, pathError := filepath.Abs(relativePath)
	if pathError != nil {
		return nil, pathError
	}

	headerStatus, statusError := os.Lstat(headerPath)
	if statusError != nil {
		return nil, statusError
	}

	headers := make(map[string]*asset.Asset)
	headerNames := tree.ReadHeaders(headerPath)
	for _, headerName := range headerNames {
		headers[headerName] = nil
	}

	header := Header{
		Name:    name,
		Hash:    tree.DeepHashFile(headerPath),
		Size:    headerStatus.Size(),
		Headers: headers,
		Sources: make(map[string]*asset.Asset),
	}

	return &header, nil
}

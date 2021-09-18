package tree

import (
	"errors"
	"os"
	"path"
	"path/filepath"
)

func FindRoot(base string) (string, error) {
	for {

		// Look for the build context in the current directory
		root := path.Join(base, ".barbican")
		if _, err := os.Stat(root); os.IsNotExist(err) == false {
			return base, nil
		}

		// Report a failure-to-find
		new_base := filepath.Dir(base)
		if base == new_base {
			return "", errors.New("couldn't find root")
		}
		base = new_base
	}
}

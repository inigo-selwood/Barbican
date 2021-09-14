package tree

import (
	"io"
	"path"

	"crypto/sha256"
	"encoding/hex"
	"path/filepath"
)

func HashRoute(realRoute string) string {

	result := ""
	for {

		// Read a token from the end of the path
		token := filepath.Base(realRoute)

		// Hash and truncate the token, adding it to the new route
		hashContext := sha256.New()
		io.WriteString(hashContext, token)
		tokenHash := hex.EncodeToString(hashContext.Sum(nil))[:10]
		result = path.Join(result, tokenHash)

		// Pop the last token from the path, or stop if they've all been read
		if token == realRoute {
			break
		}
		realRoute = filepath.Dir(realRoute)
	}

	return result
}

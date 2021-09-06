package header

import (
	"io"
	"log"
	"path"
	"regexp"
	"strings"

	"crypto/sha256"
	"encoding/hex"
	"io/ioutil"
	"path/filepath"
)

func hashRoute(realRoute string) string {

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

func readHeaders(filePath string) []string {

	// Read the file into a string
	bytes, bytesError := ioutil.ReadFile(filePath)
	if bytesError != nil {
		log.Fatalf("error reading file '%s'\n", filePath)
	}

	// Find instances of the "#include" pattern in the file
	pattern := regexp.MustCompile(`#include[ \t]*\"[^\"]+\"`)
	matches := pattern.FindAllString(string(bytes), -1)

	// Extract the text from the brackets
	var includes []string
	for _, match := range matches {
		start := strings.Index(match, "\"") + 1
		end := len(match) - 1
		includes = append(includes, match[start:end])
	}

	return includes
}

func Load(name string, route string, base string) *Header {

	// Evaluate path
	filePath := path.Join(base, route, name)

	// Read file's headers
	headers := make(map[string]*Header)
	for _, headerRoute := range readHeaders(filePath) {

		newPath := path.Join(route, headerRoute)
		newRoute := filepath.Dir(newPath)
		newName := filepath.Base(newPath)

		newHeader := Load(newName, newRoute, base)
		headers[headerRoute] = newHeader
	}

	// Create and return new header object
	header := Header{
		Name:      name,
		RealRoute: route,
		HashRoute: hashRoute(route),
		Headers:   headers,
	}
	return &header
}

package tree

import (
	"log"
	"regexp"
	"strings"

	"io/ioutil"
)

func ReadHeaders(filePath string) []string {

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

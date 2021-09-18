package tree

import (
	"crypto/sha256"
	"io"
	"log"
	"os"
)

func DeepHashFile(filePath string) string {

	// Open the file for reading
	file, fileError := os.Open(filePath)
	if fileError != nil {
		log.Fatal(fileError)
	}
	defer file.Close()

	// Hash the file contents
	hash := sha256.New()
	if _, readError := io.Copy(hash, file); readError != nil {
		log.Fatal(readError)
	}

	return string(hash.Sum(nil)[:10])
}

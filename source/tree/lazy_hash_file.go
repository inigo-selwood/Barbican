package tree

import (
	"crypto/sha256"
	"encoding/binary"
	"log"
	"os"
)

func LazyHashFile(filePath string) string {

	// Read the file's status
	fileStatus, statusError := os.Lstat(filePath)
	if statusError != nil {
		log.Fatal(statusError)
	}

	// Create a new hash context
	hash := sha256.New()

	// Add size
	size := fileStatus.Size()
	sizeBytes := make([]byte, 8)
	binary.LittleEndian.PutUint64(sizeBytes, uint64(size))
	hash.Write(sizeBytes)

	// Add modification time
	modified := fileStatus.ModTime().String()
	hash.Write([]byte(modified))

	return string(hash.Sum(nil)[:10])
}

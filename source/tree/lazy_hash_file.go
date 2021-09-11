package tree

import (
	"crypto/sha256"
    "encoding/binary"
    "log"
    "os"
)

func LazyHashFile(filePath string) string {
    fileStatus, statusError := os.Lstat(filePath)
    if statusError != nil {
        log.Fatal(statusError)
    }

    hash := sha256.New()

    size := fileStatus.Size()
    sizeBytes := make([]byte, 8)
    binary.LittleEndian.PutUint64(sizeBytes, uint64(size))
    hash.Write(sizeBytes)

    modified := fileStatus.ModTime().String()
    hash.Write([]byte(modified))

    return string(hash.Sum(nil)[:10])
}

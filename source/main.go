package main

import (
	"os"

	"github.com/inigo-selwood/barbican/command"
)

func main() {
	executionError := command.Execute()
    if executionError != nil {
        os.Exit(1)
    }
}

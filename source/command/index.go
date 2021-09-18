package command

import (
	"log"
	"fmt"

	"path/filepath"

	"github.com/spf13/cobra"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/branch"
)

func index(command *cobra.Command, arguments []string) {
	targetPath := arguments[0]
	targetName := filepath.Base(targetPath)
	targetBase := filepath.Dir(targetPath)

	targetDirectory, baseError := filepath.Abs(targetBase)
	if baseError != nil {
		log.Fatal(baseError)
	}

	contextPath, contextError := tree.FindRoot(targetDirectory)
	if contextError != nil {
		log.Fatal(contextError)
	}

	root, rootError := branch.Load(".", ".", contextPath, nil)
	if rootError != nil {
		log.Fatal(rootError)
	}

	indexError := branch.Index(root, contextPath)
	if indexError != nil {
		log.Fatal(indexError)
	}

	branch.Display(root, "", true, true)

	fmt.Printf("barbican: indexed '%s'\n", targetName)
}

var indexCommand = &cobra.Command{
	Use:   "index [target]",
	Short: "Indexes a build target",
	Long:  "Traces dependencies, detects changes, and cleans the build space",
	Args:  cobra.ExactArgs(1),
	Run:   index,
}

func init() {
	rootCommand.AddCommand(indexCommand)
}

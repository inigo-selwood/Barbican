package command

import (
	"log"
	"errors"

	"path/filepath"

	"github.com/spf13/cobra"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/branch"
)

func index(command *cobra.Command, arguments []string) {

	// Evaluate target path, directory, and name
	targetPath := arguments[0]
	targetBase := filepath.Dir(targetPath)

	targetDirectory, baseError := filepath.Abs(targetBase)
	if baseError != nil {
		baseError := errors.New("barbican: couldn't evaluate base path")
		log.Fatal(baseError)
	}

	contextPath, contextError := tree.FindRoot(targetDirectory)
	if contextError != nil {
		rootError := errors.New("barbican: couldn't find context")
		log.Fatal(rootError)
	}

	// Load context as tree
	root, rootError := branch.Load(".", contextPath, nil)
	if rootError != nil {
		loadError := errors.New("barbican: couldn't load build tree")
		log.Fatal(loadError)
	}

	// Index and print tree
	indexError := branch.Index(root, contextPath)
	if indexError != nil {
		linkError := errors.New("barbican: couldn't index build tree")
		log.Fatal(linkError)
	}
	branch.Display(root, "", true, true)
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

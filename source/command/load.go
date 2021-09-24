package command

import (
	"log"
	"os"
	"errors"

	"path/filepath"

	"github.com/spf13/cobra"

	"github.com/inigo-selwood/barbican/tree"
	"github.com/inigo-selwood/barbican/tree/branch"
)

func load(command *cobra.Command, arguments []string) {

	// Evaluate base directory for build context
	workingDirectory, directoryError := os.Getwd()
	if directoryError != nil {
		baseError := errors.New("barbican: couldn't evaluate working directory")
		log.Fatal(baseError)
	}

	var baseDirectory string
	if len(arguments) == 1 {
		baseRoute := arguments[0]
		basePath := filepath.Join(workingDirectory, baseRoute)

		var baseError error
		baseDirectory, baseError = filepath.Abs(basePath)
		if baseError != nil {
			absoluteError := errors.New("barbican: couldn't evaluate base path")
			log.Fatal(absoluteError)
		}
	} else {
		baseDirectory = workingDirectory
	}

	context, contextError := tree.FindRoot(baseDirectory)
	if contextError != nil {
		contextError := errors.New("barbican: couldn't find context")
		log.Fatal(contextError)
	}

	// Create tree from build context
	root, rootError := branch.Load(".", context, nil)
	if rootError != nil {
		loadError := errors.New("failed to load tree")
		log.Fatal(loadError)
	}
	branch.Display(root, "", true, true)
}

var loadCommand = &cobra.Command{
	Use:   "load",
	Short: "Loads a build context",
	Long:  "Makes a data structure from the build context filesystem",
	Run:   load,
	Args:  cobra.MaximumNArgs(1),
}

func init() {
	rootCommand.AddCommand(loadCommand)
}

package command

import (
	"fmt"
	"log"
	"path/filepath"

	"github.com/spf13/cobra"

	"github.com/inigo-selwood/barbican/tree/header"
	"github.com/inigo-selwood/barbican/tree/root"
)

func index(command *cobra.Command, arguments []string) {
	targetPath := arguments[0]
	targetDirectory := filepath.Dir(targetPath)
	contextBase, contextBaseError := root.Find(targetDirectory)
	if contextBaseError != nil {
		log.Fatal("couldn't find context")
	}

	targetRoute, routeError := filepath.Rel(contextBase, targetDirectory)
	if routeError != nil {
		log.Fatal("couldn't resolve target path within context")
	}

	targetName := filepath.Base(targetPath)
	target := header.Load(targetName, targetRoute, targetDirectory)

	fmt.Printf("barbican: indexed '%s'\n", target.Name)
}

var indexCommand = &cobra.Command{
	Use:   "index [target]",
	Short: "Indexes a build target",
	Long:  "Traces dependencies, detects changes, and cleans the build space",
	Args:  cobra.ExactArgs(1),
	Run:   index,
}

func init() {
	indexCommand.Flags().StringP("target", "t", "", "target to index")
	rootCommand.AddCommand(indexCommand)
}

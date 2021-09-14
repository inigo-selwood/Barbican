package command

import (
	"fmt"
	"path/filepath"

	"github.com/spf13/cobra"
)

func index(command *cobra.Command, arguments []string) {
	targetPath := arguments[0]
	targetName := filepath.Base(targetPath)
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

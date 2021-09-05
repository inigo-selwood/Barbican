package command

import (
	"fmt"

	"github.com/spf13/cobra"
)

func index(command *cobra.Command, arguments []string) {
	fmt.Println("barbican: indexing")
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

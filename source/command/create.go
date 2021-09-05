package command

import (
	"fmt"

	"github.com/spf13/cobra"
)

func create(command *cobra.Command, arguments []string) {
	fmt.Println("barbican: creating")
}

var createCommand = &cobra.Command{
	Use:   "create [base]",
	Short: "Creates a build environment",
	Long:  "Creates and configures a build environment in a given directory",
	Args:  cobra.MaximumNArgs(1),
	Run:   create,
}

func init() {
	rootCommand.AddCommand(createCommand)
}

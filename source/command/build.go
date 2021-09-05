package command

import (
	"fmt"

	"github.com/spf13/cobra"
)

func build(command *cobra.Command, arguments []string) {
	fmt.Println("barbican: building")
}

var buildCommand = &cobra.Command{
	Use:   "build [target]",
	Short: "Builds a C/C++ binary or static library",
	Long:  "Compiles a target, and building and linking its dependencies",
	Args:  cobra.ExactArgs(1),
	Run:   build,
}

func init() {
	rootCommand.AddCommand(buildCommand)
}

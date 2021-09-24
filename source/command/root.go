package command

import (
	"github.com/spf13/cobra"
)

var rootCommand = &cobra.Command{
	Use:   "barbican",
	Short: "A build manager for C/C++",
	Long:  "Simple, parallel build manager for binaries and static libraries",
}

func Execute() error {
	return rootCommand.Execute()
}

func init() {
	rootCommand.CompletionOptions.DisableDefaultCmd = true
}

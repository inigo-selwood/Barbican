package command

import (
	"github.com/spf13/cobra"
)

var rootCommand = &cobra.Command{
	Use:   "barbican",
	Short: "A build manager for C/C++",
	Long:  "Simple, parallel build manager for binaries and static libraries",
}

func Execute() {
	cobra.CheckErr(rootCommand.Execute())
}

func init() {
	rootCommand.CompletionOptions.DisableDefaultCmd = true
}

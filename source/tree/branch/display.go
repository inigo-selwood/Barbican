package branch

import (
	"fmt"

	"github.com/inigo-selwood/barbican/tree/asset/header"
	"github.com/inigo-selwood/barbican/tree/asset/source"
)

func Display(branch *Branch, leader string, final bool, root bool) {

	// Print starter
	starter := ""
	if root == false {
		if final {
			starter = "╰─ "
		} else {
			starter = "├─ "
		}
	}

	// Print the branch name
	fmt.Printf("%s%s%s\n", leader, starter, branch.Name)

	// Evaluate a new leader
	newLeader := ""
	if root == false {
		if final {
			newLeader = leader + "   "
		} else {
			newLeader = leader + "│  "
		}
	}

	// Print each child branch
	index := 0
	count := len(branch.Headers) + len(branch.Sources) + len(branch.Branches)
	for _, childBranch := range branch.Branches {
		finalBranch := (index + 1) == count
		Display(childBranch, newLeader, finalBranch, false)
		index += 1
	}

	// Print headers
	for _, instance := range branch.Headers {
		finalFile := (index + 1) == count
		header.Display(instance, newLeader, finalFile)
		index += 1
	}

	// Print sources
	for _, instance := range branch.Sources {
		finalFile := (index + 1) == count
		source.Display(instance, newLeader, finalFile)
		index += 1
	}
}

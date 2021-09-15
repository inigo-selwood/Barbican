package branch

import (
	"fmt"

	"github.com/inigo-selwood/barbican/tree/asset/header"
	"github.com/inigo-selwood/barbican/tree/asset/source"
)

func Display(branch *Branch, leader string, final bool, root bool) {
	starter := ""
	if root == false {
		if final {
			starter = "╰─ "
		} else {
			starter = "├─ "
		}
	}

	fmt.Printf("%s%s%s\n", leader, starter, branch.Name)

	newLeader := ""
	if root == false {
		if final {
			newLeader = leader + "   "
		} else {
			newLeader = leader + "│  "
		}
	}

	index := 0
	count := len(branch.Headers) + len(branch.Sources) + len(branch.Branches)
	for _, childBranch := range branch.Branches {
		finalBranch := (index + 1) == count
		Display(childBranch, newLeader, finalBranch, false)
		index += 1
	}

	for _, instance := range branch.Headers {
		finalFile := (index + 1) == count
		header.Display(instance, newLeader, finalFile)
		index += 1
	}

	for _, instance := range branch.Sources {
		finalFile := (index + 1) == count
		source.Display(instance, newLeader, finalFile)
		index += 1
	}
}

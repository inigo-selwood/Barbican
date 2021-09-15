package source

import "fmt"

func Display(instance *Source, leader string, final bool) {
	starter := ""
	if final {
		starter = "╰─ "
	} else {
		starter = "├─ "
	}

	fmt.Printf("%s%s%s\n", leader, starter, instance.Name)

	for headerName, _ := range instance.Headers {
		newLeader := ""
		if final {
			newLeader = leader + "   "
		} else {
			newLeader = leader + "│  "
		}

		fmt.Printf("%s→ %s\n", newLeader, headerName)
	}
}

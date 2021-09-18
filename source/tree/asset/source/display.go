package source

import "fmt"

func Display(instance *Source, leader string, final bool) {

	// Evaluate starter
	starter := ""
	if final {
		starter = "╰─ "
	} else {
		starter = "├─ "
	}

	// Print source name
	fmt.Printf("%s%s%s\n", leader, starter, instance.Name)

	// Print headers
	for headerName, _ := range instance.Headers {
		newLeader := ""
		if final {
			newLeader = leader + "   "
		} else {
			newLeader = leader + "│  "
		}

		fmt.Printf("%s\u001b[36m→\u001b[0m %s\n", newLeader, headerName)
	}
}

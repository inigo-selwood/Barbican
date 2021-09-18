package header

import "fmt"

func Display(instance *Header, leader string, final bool) {
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

		fmt.Printf("%s\u001b[36m→\u001b[0m %s\n", newLeader, headerName)
	}

	for sourceName, _ := range instance.Sources {
		newLeader := ""
		if final {
			newLeader = leader + "   "
		} else {
			newLeader = leader + "│  "
		}

		fmt.Printf("%s\u001b[33m←\u001b[0m %s\n", newLeader, sourceName)
	}
}

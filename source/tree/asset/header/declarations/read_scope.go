package declarations

import "github.com/inigo-selwood/barbican/buffer"

func readScope(context *buffer.Buffer) string {
    startIndex := context.Index
    result := ""

    for {
		token := readIdentifier(context)
		if token == "" {
			context.Index = startIndex
			return ""
		}
		result += token

		if buffer.SkipString(context, "::") == false {
			break
		}
		result = result + "::"
	}

    return result
}

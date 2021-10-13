package declarations

import "github.com/inigo-selwood/barbican/buffer"

func readIdentifier(context *buffer.Buffer) string {
	result := ""
	for {
		if buffer.EndReached(context) {
			break
		}

		character := buffer.PeekCharacter(context)
		if (character < 'a' || character > 'z') &&
			(character < 'A' || character > 'Z') &&
			(result == "" || character < '0' || character > '9') &&
			character != '_' {

			break;
		}

		result += string(buffer.ReadCharacter(context))
	}

	return result
}

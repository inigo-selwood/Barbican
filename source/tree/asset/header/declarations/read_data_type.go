package declarations

import (
	"errors"

	"github.com/inigo-selwood/barbican/buffer"
)

func readDataType(context *buffer.Buffer) (string, error) {
	startIndex := context.Index
	result := ""

	// Skip const specifiers
	if buffer.SkipString(context, "const") {
		result += "const "

		if buffer.SkipSpace(context) == false {
			context.Index = startIndex
			return "", errors.New("no space after const specifier")
		}
	}

	// Handle modifiers for POD types
	// To do: make unique to relevant types (ie: char, int)
	modifiers := []string{
		"unsigned",
		"signed",
		"short",
		"long",
	}
	for _, modifier := range modifiers {
		if buffer.SkipString(context, modifier) {
			result += modifier + " "

			if buffer.SkipSpace(context) == false {
				context.Index = startIndex
				return "", errors.New("no space after modifier")
			}

			break
		}
	}

	// Read the data type, including scope
	buffer.SkipSpace(context)
	scopedType := readScope(context)
	if scopedType == "" {
		context.Index = startIndex
		return "", errors.New("no data type")
	}
	result += scopedType

	// Handle any templated parameters
	if buffer.SkipCharacter(context, '<') {
		result = result + "<"

		for {
			buffer.SkipSpace(context)
			template, templateError := readDataType(context)
			if templateError != nil{
				context.Index = startIndex
				return "", templateError
			}
			result = result + template

			buffer.SkipSpace(context)
			if buffer.SkipCharacter(context, ',')  == false {
				break
			}
			result = result + ", "
		}

		buffer.SkipSpace(context)
		if buffer.SkipCharacter(context, '>') == false {
			context.Index = startIndex
			return "", errors.New("expected template closure")
		}
		result = result + ">"
	}

	// Add memory modifiers (pointers, references)
	lastIndex := context.Index
	pointers := ""
	for {
		buffer.SkipSpace(context)
		character := buffer.PeekCharacter(context)
		if character != '*' && character != '&' {
			context.Index = lastIndex
			break
		}

		pointers = pointers + string(character)
		buffer.Increment(context)
		lastIndex = context.Index
	}
	if pointers != "" {
		result = result + " " + pointers
	}

	return result, nil
}

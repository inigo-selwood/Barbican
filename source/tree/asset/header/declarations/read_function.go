package declarations

import (
	"errors"

	"github.com/inigo-selwood/barbican/buffer"
)

func readArgumentPack(context *buffer.Buffer) (string, error) {
	startIndex := context.Index
	result := ""

	if buffer.SkipCharacter(context, '(') == false {
		return "", errors.New("no opening bracket for argument pack")
	}
	result += "("

	for {
		buffer.SkipSpace(context)
		dataType, typeError := readDataType(context)
		if typeError != nil {
			break
		}
		result += dataType

		buffer.SkipSpace(context)
		name := readIdentifier(context)
		if name == "" {
			context.Index = startIndex
			return "", errors.New("no name for argument")
		}
		result += " " + name

		buffer.SkipSpace(context)
		if buffer.SkipCharacter(context, ',') == false {
			break
		}
		result += ", "
	}

	buffer.SkipSpace(context)
	if buffer.SkipCharacter(context, ')') == false {
		context.Index = startIndex
		return "", errors.New("no closing bracket after argument pack")
	}
	result += ")"

	return result, nil
}

func readFunction(context *buffer.Buffer) (string, error) {
	startIndex := context.Index
	result := ""

	/*
	// Check for virtual specifier
	buffer.SkipSpace(context)
	if buffer.SkipString(context, "virtual") {
		result += "virtual "

		if buffer.SkipSpace(context) == false {
			context.Index = startIndex
			return ""
		}
	}
	*/

	// Read return type
	// To do: only make optional in the case of constructors
	returnType, typeError := readDataType(context)
	if typeError != nil {
		context.Index = startIndex
		return "", errors.New("no function data type")
	}
	result += returnType

	// Read function name
	buffer.SkipSpace(context)
	functionName := readScope(context)
	if functionName == "" {
		context.Index = startIndex
		return "", errors.New("no function name")
	}
	result += " " + functionName

	// Read arguments
	buffer.SkipSpace(context)
	argumentPack, argumentsError := readArgumentPack(context)
	if argumentsError != nil {
		context.Index = startIndex
		return "", argumentsError
	}
	result += argumentPack

	/*
	// Check for const, override specifiers
	buffer.SkipSpace(context)
	if buffer.SkipString(context, "const") {
		result += " const"
	}

	buffer.SkipSpace(context)
	if buffer.SkipString(context, "override") {
		result += " override"
	}
	*/

	buffer.SkipSpace(context)
	if buffer.SkipCharacter(context, ';') == false {
		context.Index = startIndex
		return "", errors.New("no semi-colon after function (ie: definition)")
	}

	return result, nil
}

package buffer

func skipLine(context *Buffer) {
    if SkipString(context, "//") == false {
        return
    }

    for {

        // Stop when end-of-file or end-of-line reached
        if context.Index == context.Length {
            return
        } else if context.Text[context.Index] == '\n' {
            return
        }

        context.Index += 1
    }
}

func skipComment(context *Buffer) {

    // Skip comment start
    if SkipString(context, "/*") == false {
        return
    }

    // Increment until '*/' encountered
    for {
        if context.Index == context.Length {
            return
        } else if SkipString(context, "*/") {
            return
        }

        context.Index += 1
    }
}

// Skips whitespace and C-style comments
func SkipSpace(context *Buffer) bool {
    offset := 0

    for {

        // Stop if end-of-buffer reached
        if EndReached(context) {
            break
        }

        // Skip inline comments
        if MatchString(context, "//") {
            skipLine(context)

        // Skip multi-line comments
        } else if MatchString(context, "/*") {
            skipComment(context)

        // Skip whitespace characters
        } else {
            character := PeekCharacter(context)
            if character != ' ' &&
                character != '\t' &&
                character != '\v' &&
                character != '\r' &&
                character != '\n' {

                break
            }

            offset += 1
            context.Index += 1
        }
    }

    return offset != 0
}

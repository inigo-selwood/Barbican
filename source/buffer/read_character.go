package buffer

// Reads the character at the buffer's current position, incrementing
func ReadCharacter(context *Buffer) rune {
    if context.Index == context.Length {
        return 0
    }

    result := rune(context.Text[context.Index])
    context.Index += 1
    return result
}

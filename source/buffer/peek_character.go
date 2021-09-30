package buffer

// Looks at the next character in the buffer without incrementing
func PeekCharacter(context *Buffer) rune {
    if context.Index == context.Length {
        return 0
    }

    return rune(context.Text[context.Index])
}

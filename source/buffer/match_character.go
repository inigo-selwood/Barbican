package buffer

// Checks whether a given character exists at the buffer's position
func MatchCharacter(context *Buffer, character rune) bool {
    if context.Index == context.Length {
        return false
    }

    return context.Text[context.Index] == byte(character)
}

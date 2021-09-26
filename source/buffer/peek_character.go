package buffer

func PeekCharacter(context *Buffer, character rune) bool {
    if context.Index == context.Length {
        return false
    }

    return context.Text[context.Index] == byte(character)
}

package buffer

func ReadCharacter(context *Buffer, character rune) bool {
    if context.Index == context.Length {
        return false
    }

    var result bool = context.Text[context.Index] == byte(character)
    if result {
        context.Index += 1
    }
    return result
}

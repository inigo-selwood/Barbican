package buffer

// Checks for -- and if found, increments past -- a given string
func SkipString(context *Buffer, text string) bool {
    textLength := len(text)

    if context.Index + textLength >= context.Length {
        return false
    }

    for offset := 0; offset < textLength; offset += 1 {
        if context.Text[context.Index + offset] != text[offset] {
            return false
        }
    }

    context.Index += textLength
    return true
}

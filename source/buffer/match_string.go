package buffer

// Checks if a given string exists at the buffer's current position
func MatchString(context *Buffer, text string) bool {
    textLength := len(text)

    if context.Index + textLength >= context.Length {
        return false
    }

    for offset := 0; offset < textLength; offset += 1 {
        if context.Text[context.Index + offset] != text[offset] {
            return false
        }
    }

    return true
}

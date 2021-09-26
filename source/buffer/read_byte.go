package buffer

func ReadByte(context *Buffer) byte {
    if context.Index == context.Length {
        return 0
    }

    return context.Text[context.Index]
}

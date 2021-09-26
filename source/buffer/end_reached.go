package buffer

func EndReached(context *Buffer) bool {
    return context.Index == context.Length
}

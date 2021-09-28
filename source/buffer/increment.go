package buffer

func Increment(context *Buffer) {
    if context.Index == context.Length {
        return
    }

    context.Index += 1
}

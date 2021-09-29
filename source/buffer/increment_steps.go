package buffer

// Increments a given number of steps
func IncrementSteps(context *Buffer, steps int) {
    if steps <= 0 {
        return
    }

    context.Index += steps
    if context.Index > context.Length {
        context.Index = context.Length
    }
}

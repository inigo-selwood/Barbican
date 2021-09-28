package buffer

// Increments a given number of steps
func IncrementSteps(context *Buffer, steps int) {
    if steps <= 0 {
        return
    }

    for step := 0; step < steps; step += 1 {
        if context.Index == context.Length {
            return
        }

        context.Index += 1
    }
}

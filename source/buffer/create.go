package buffer

func Create(text string) Buffer {
    result := Buffer{
        Text:   text,
        Index:  0,
        Length: len(text),
    }

    return result
}

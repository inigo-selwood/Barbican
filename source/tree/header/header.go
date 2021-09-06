package header

type Header struct {
	Name string

	RealRoute string
	HashRoute string

	Headers map[string]*Header
}

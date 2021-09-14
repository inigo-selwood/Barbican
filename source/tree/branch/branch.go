package branch

import (
	"github.com/inigo-selwood/barbican/tree/asset/header"
	"github.com/inigo-selwood/barbican/tree/asset/source"
)

type Branch struct {
	Name string

	Size int64

	Headers map[string]*header.Header
	Sources map[string]*source.Source

	Branches map[string]*Branch
}

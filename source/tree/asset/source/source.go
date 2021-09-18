package source

import "github.com/inigo-selwood/barbican/tree/asset"

type Source struct {
	Name string
	Hash string

	Size int64

	Dirty bool

	Headers map[string]asset.Asset
}

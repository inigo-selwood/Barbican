package source

import "github.com/inigo-selwood/barbican/tree/asset"

type Source struct {
	Name string
	Hash string

	Size int64

	Headers map[string]*asset.Asset
}

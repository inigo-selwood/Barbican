package header

import "github.com/inigo-selwood/barbican/tree/asset"

type Header struct {
	Name string
	Hash string

	Size int64

	Headers map[string]*asset.Asset
	Sources map[string]*asset.Asset
}

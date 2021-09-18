package branch

import (
    // "path/filepath"

    "github.com/inigo-selwood/barbican/tree/asset"
    "github.com/inigo-selwood/barbican/tree/asset/header"
    "github.com/inigo-selwood/barbican/tree/asset/source"
)

func indexHeader(headerInstance *header.Header, parent *Branch) error {
    for headerRoute, _ := range headerInstance.Headers {
        header, findError := Find(headerRoute, parent)
        if findError != nil {
            return findError
        }

        headerInstance.Headers[headerRoute] = asset.Asset(header)
    }

    return nil
}

func indexSource(sourceInstance *source.Source, parent *Branch) error {
    for headerRoute, _ := range sourceInstance.Headers {
        header, findError := Find(headerRoute, parent)
        if findError != nil {
            return findError
        }

        header.Sources[sourceInstance.Name] = asset.Asset(sourceInstance)
        sourceInstance.Headers[headerRoute] = asset.Asset(header)
    }

    return nil
}

func Index(branchInstance *Branch, root string) error {


    for _, headerInstance := range branchInstance.Headers {
        indexError := indexHeader(headerInstance, branchInstance)
        if indexError != nil {
            return indexError
        }
    }

    for _, sourceInstance := range branchInstance.Sources {
        indexError := indexSource(sourceInstance, branchInstance)
        if indexError != nil {
            return indexError
        }
    }

    for _, childBranch := range branchInstance.Branches {
        Index(childBranch, root)
    }

    return nil
}

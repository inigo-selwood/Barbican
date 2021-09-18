package branch

import (
    "github.com/inigo-selwood/barbican/tree/asset"
    "github.com/inigo-selwood/barbican/tree/asset/header"
    "github.com/inigo-selwood/barbican/tree/asset/source"
)

func indexHeader(headerInstance *header.Header, parent *Branch, root string) error {

    // Emplace a pointer for each header
    for headerRoute, _ := range headerInstance.Headers {
        _, instance, findError := Find(headerRoute, parent)
        if findError != nil {
            return findError
        }

        headerInstance.Headers[headerRoute] = asset.Asset(instance)
    }

    return nil
}

func indexSource(sourceInstance *source.Source, parent *Branch, root string) error {

    // Emplace a pointer for each header (linking implementation sources)
    for headerRoute, _ := range sourceInstance.Headers {
        instanceBranch, instance, findError := Find(headerRoute, parent)
        if findError != nil {
            return findError
        }

        sourceInstance.Headers[headerRoute] = asset.Asset(instance)
        if instanceBranch == parent {
            instance.Sources[sourceInstance.Name] = asset.Asset(sourceInstance)
        }
    }

    return nil
}

func Index(branchInstance *Branch, root string) error {

    // Index headers
    for _, headerInstance := range branchInstance.Headers {
        indexError := indexHeader(headerInstance, branchInstance, root)
        if indexError != nil {
            return indexError
        }
    }

    // Index sources
    for _, sourceInstance := range branchInstance.Sources {
        indexError := indexSource(sourceInstance, branchInstance, root)
        if indexError != nil {
            return indexError
        }
    }

    // Index child branches
    for _, childBranch := range branchInstance.Branches {
        indexError := Index(childBranch, root)
        if indexError != nil {
            return indexError
        }
    }

    return nil
}

package branch

import (
    "fmt"
    "errors"
    "strings"

    "github.com/inigo-selwood/barbican/tree/asset/header"
)

func trim(route string) (string, string) {

    // Get the index of the first slash
    endIndex := strings.Index(route, "/")
    if endIndex == -1 {
        return route, ""
    }

    // Split the route into a token and a remaining route
    token := route[:endIndex]
    newRoute := route[(endIndex + 1):]

    return token, newRoute
}

func Find(route string, context *Branch) (*Branch, *header.Header, error) {
    if context == nil {
        return nil, nil, errors.New("nil context")
    }

    token, newRoute := trim(route)

    // If the last token has been extracted, try to find the header in the
    // current branch
    if newRoute == "" {
        header, headerFound := context.Headers[token]
        if headerFound == false {
            error := fmt.Errorf("no such header '%s' in '%s'",
                    token,
                    context.Name)
            return nil, nil, error
        }

        return context, header, nil

    // Handle arent-routing tokens
    } else if token == ".." {
        if context.Parent == nil {
            return nil, nil, errors.New("import outside context requested")
        }

        return Find(newRoute, context.Parent)

    // Handle self-routing tokens
    } else if token == "." {
        return Find(newRoute, context)
    }

    // Otherwise, try to delegate to a sub-branch
    newContext, contextFound := context.Branches[token]
    if contextFound == false {
        error := fmt.Errorf("no such branch '%s' in '%s'",
                token,
                context.Name)
        return nil, nil, error
    }

    return Find(newRoute, newContext)
}

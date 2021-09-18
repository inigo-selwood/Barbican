package branch

import (
    "fmt"
    "errors"
    "strings"

    "github.com/inigo-selwood/barbican/tree/asset/header"
)

func trim(route string) (string, string) {
    endIndex := strings.Index(route, "/")
    if endIndex == -1 {
        return route, ""
    }

    token := route[:endIndex]
    newRoute := route[(endIndex + 1):]

    return token, newRoute
}

func Find(route string, context *Branch) (*header.Header, error) {
    if context == nil {
        return nil, errors.New("nil context")
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
            return nil, error
        }

        return header, nil

    // Handle arent-routing tokens
    } else if token == ".." {
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
        return nil, error
    }

    return Find(newRoute, newContext)
}

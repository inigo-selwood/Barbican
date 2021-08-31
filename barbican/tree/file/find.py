from typing import Tuple

from tree.branch.branch import Branch


def _get_token(route: str) -> Tuple[str, str]:
    end = route.find('/')
    if end == -1:
        return route, ''

    token = route[:end]
    new_route = route[(end + 1):]

    return (token, new_route)


def find(route: str, branch: Branch):
    token, new_route = _get_token(route)

    if not new_route:
        if token not in branch.headers:
            return None

        return branch.headers[token]

    elif token == '.':
        return find(new_route, branch)

    elif token == '..':
        if not token.parent:
            return None

        return find(new_route, branch.parent)

    else:
        if token not in branch.branches:
            return None

        return find(new_route, branch.branches[token])

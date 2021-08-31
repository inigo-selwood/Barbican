import os
import hashlib

from tree.branch.branch import Branch
from tree.branch.display import display

# from tree.file.header.header import Header
# from tree.file.source.source import Source

from tree.file.load import load as load_file


def load(root: str, route: str, parent: Branch = None) -> Branch:

    path = os.path.join(root, route)

    branch = Branch()
    branch.name = os.path.basename(path)
    branch.parent = parent
    branch.route = route

    hashes = []
    for entry_name in os.listdir(path):

        entry_route = os.path.join(route, entry_name)
        if os.path.isdir(entry_route):

            if entry_name == '.barbican':
                continue

            new_branch = load(root, entry_route, branch)
            branch.branches[entry_name] = new_branch
            hashes.append(new_branch.hash)

        elif os.path.isfile(entry_route):
            _, extension = os.path.splitext(entry_name)

            if extension in ['.hpp', '.hh', '.h']:
                file = load_file(root, entry_name, branch)
                file.type = 'header'
                file.attributes['headers'] = {}
                file.attributes['sources'] = {}

                branch.headers[entry_name] = file
                hashes.append(file.hash)

            elif extension in ['.cpp', '.cc', '.c']:
                file = load_file(root, entry_name, branch)
                file.type = 'source'
                file.attributes['headers'] = {}

                branch.sources[entry_name] = file
                hashes.append(file.hash)

            else:
                continue

    context = hashlib.shake_128()
    for hash in sorted(hashes):
        context.update(hash.encode())
    branch.hash = context.hexdigest(5)

    return branch

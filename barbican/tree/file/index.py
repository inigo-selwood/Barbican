import os

from tree.file.file import File

from tree.branch.route.get_source import get_source as get_source_route
from tree.file.find import find as find_file
from tree.utilities.read_includes import read_includes


def index(file: File, root: str) -> bool:

    file_base = get_source_route(file.parent)
    file_path = os.path.join(root, file_base, file.name)

    if file.type == 'header':
        include_routes = read_includes(file_path)

        for include in include_routes:
            header = find_file(include, file.parent)
            if not header:
                print(f"barbican: '{include}' in '{file_path}' unresolved")
                return False

            file.attributes['headers'][include] = header

    elif file.type == 'source':
        include_routes = read_includes(file_path)

        for include in include_routes:
            header = find_file(include, file.parent)
            if not header:
                print(f"barbican: '{include}' in '{file_path}'")
                return False

            file.attributes['headers'][include] = header

            header_base = get_source_route(header.parent)
            route = os.path.relpath(file_path, start=header_base)

            if header_base == file_base:
                header.attributes['sources'][route] = file

    return True

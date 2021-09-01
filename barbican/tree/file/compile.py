from tree.file.build import build
from tree.file.file import File


def compile(file: File, root: str):

    if file.type == 'source':
        for header in file.attributes['headers'].values():
            build(header, root)

    elif file.type == 'header':
        build(header, root)

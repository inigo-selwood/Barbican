
def build(file: File, root: str):

    if file.type == 'header':
        for header in file.attributes['headers']:
            build(header, root)

    elif file.type == 'source':

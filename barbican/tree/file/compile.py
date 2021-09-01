import os
import asyncio

from tree.file.build import build
from tree.file.file import File

from tree.branch.route.get_build import get_build as get_build_route
from tree.branch.route.get_source import get_source as get_source_route

async def _compile_source(file: File, root: str):

    source_build_base = get_build_route(file.parent)
    source_build_path = os.path.join(source_build_base, file.hash)

    command = [
        'clang++'
    ]

    for header in file.attributes['headers'].values():

        if file.name in header.attributes['sources']:
            raise Exception('barbican: source is part of a build tree')

        header_base = get_build_route(header.parent)
        header_path = os.path.join(root, header_base, f'{header.hash}.o')
        header_route = os.path.relpath(header_path, start=source_build_base)
        command.append(header_route)

    name, _ = os.path.splitext(file.name)
    source_active_base = get_source_route(file.parent)
    source_route = os.path.relpath(source_active_base, source_build_base)
    command.extend(['-o', os.path.join(source_route, name)])

    source_active_base = get_source_route(file.parent)
    source_path = os.path.join(root, source_active_base, file.name)
    source_route = os.path.relpath(source_path, source_build_base)
    command.append(source_route)

    flags = [
        '-Wall',
        '-g3',
        '-O0',
        '-std=c++17'
    ]
    command.extend(flags)

    print(' '.join(command))

    process = await asyncio.create_subprocess_shell(' '.join(command),
            cwd=source_build_base,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        print(stdout.decode())
        print(stderr.decode())
        print('uh-oh')
        return False

    return True

def compile(file: File, root: str):

    if file.type == 'source':
        for header in file.attributes['headers'].values():
            build(header, root)

        asyncio.run(_compile_source(file, root))

    elif file.type == 'header':
        build(header, root)

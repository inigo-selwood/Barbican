import os
import asyncio

from tree.file.file import File
from tree.branch.route.get_build import get_build as get_build_route
from tree.branch.route.get_source import get_source as get_source_route

processing = []
resolved = []


async def _build_source(file: File, root: str):

    source_build_base = get_build_route(file.parent)
    source_build_path = os.path.join(source_build_base, f'{file.hash}.o')
    if os.path.isfile(source_build_path):
        return True

    command = [
        'clang++'
    ]

    for header in file.attributes['headers'].values():

        if file.name in header.attributes['sources']:
            continue

        header_base = get_build_route(header.parent)
        header_path = os.path.join(root, header_base, f'{header.hash}.o')
        header_route = os.path.relpath(header_path, start=source_build_base)
        command.append(header_route)

    command.extend(['-o', f'{file.hash}.o'])

    source_active_base = get_source_route(file.parent)
    source_path = os.path.join(root, source_active_base, file.name)
    source_route = os.path.relpath(source_path, source_build_base)
    command.extend(['-c', source_route])

    flags = [
        '-Wall',
        '-g3',
        '-O0',
        '-std=c++17'
    ]
    command.extend(flags)
    command.append(f'# {file.name}')

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


async def _build_header(file: File, root: str):

    if file.hash in resolved:
        return
    elif file.hash in processing:
        raise Exception('circular inclusion')

    header_build_base = get_build_route(file.parent)
    header_build_path = os.path.join(header_build_base, f'{file.hash}.o')
    if os.path.isfile(header_build_path):
        return True

    headers = {}
    for header in file.attributes['headers'].values():
        headers[header.hash] = header

    for source in file.attributes['sources'].values():
        for header in source.attributes['headers'].values():
            if header.hash == file.hash or header.hash in headers:
                continue

            headers[header.hash] = header

    for header in headers.values():
        if await _build_header(header, root) == False:
            return False

    source_coroutines = []
    for source in file.attributes['sources'].values():
        source_coroutines.append(_build_source(source, root))

    results = await asyncio.gather(*source_coroutines)
    if False in results:
        return False

    command = [
        'ld',
        '-r'
    ]

    for source in file.attributes['sources'].values():
        command.append(f'{source.hash}.o')

    for header in file.attributes['headers'].values():
        base = get_build_route(header.parent)
        path = os.path.join(base, f'{header.hash}.o')
        route = os.path.relpath(path, start=header_build_base)
        command.append(route)

    command.extend(['-o', f'{file.hash}.o'])

    print(' '.join(command))
    header_active_base = get_source_route(file.parent)
    process = await asyncio.create_subprocess_shell(' '.join(command),
            cwd=header_build_base,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        print(stdout.decode())
        print(stderr.decode())
        print('uh-oh')
        return False

    return True


def build(file: File, root: str):

    if file.type == 'header':
        asyncio.run(_build_header(file, root))
    elif file.type == 'source':
        asyncio.run(_build_source(file, root))

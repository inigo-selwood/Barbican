import hashlib

def hash(file: str) -> str:

    BLOCK_SIZE = 65536

    file_hash = hashlib.shake_256()
    with open(file, 'rb') as file:

        block = file.read(BLOCK_SIZE)
        while len(block):
            file_hash.update(block)
            block = file.read(BLOCK_SIZE)

    return file_hash.hexdigest(8)

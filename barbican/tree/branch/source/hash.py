import hashlib


def hash(file: str) -> str:

    # Limits the number of bytes that are read at once
    BLOCK_SIZE = 65536

    # Update a hash object for each block in the file
    file_hash = hashlib.shake_256()
    with open(file, 'rb') as file:

        block = file.read(BLOCK_SIZE)
        while len(block):
            file_hash.update(block)
            block = file.read(BLOCK_SIZE)

    return file_hash.hexdigest(8)

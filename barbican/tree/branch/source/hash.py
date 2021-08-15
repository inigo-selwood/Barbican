import hashlib


def hash(file: str) -> str:

    """ Hash the contents of a file

    Arguments
    ---------
    file: str
        the absolute path of the file to hash

    Returns
    -------
    hash: str
        the hash generated (16 hexadecimal characters long)
    """

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

import os
import hashlib

from datetime import datetime


def hash_file(path: str):
    status = os.lstat(path)
    modified = datetime.fromtimestamp(status.st_mtime)
    size = status.st_size

    context = hashlib.shake_128()
    context.update(bytes(size))
    context.update(modified.__str__().encode())

    hash = context.hexdigest(5)
    return hash

import sys
import hashlib


def hash_file(path: str):
    
    BUFFER_SIZE = 65536
    context = hashlib.shake_256()
    with open(path, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break

            context.update(data)

    return context.hexdigest(5)

from enum import Enum


class Status(Enum):
    UNCHANGED = 0
    ALTERED = 1
    ADDED = 2
    REMOVED = 3

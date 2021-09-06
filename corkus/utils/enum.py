from enum import Enum

class CorkusEnum(Enum):
    def __int__(self) -> int:
        for i, elem in enumerate(reversed(self.__class__)):
            if elem == self:
                return i
        return 0

    def __lt__(self, obj: object) -> bool:
        if not isinstance(obj, self.__class__):
            return NotImplemented
        return int(self) < int(obj)

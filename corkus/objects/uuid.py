from typing import Optional
from uuid import UUID

class CorkusUUID(UUID):
    def __init__(self, uuid: str) -> None:
        super().__init__(uuid)

    def string(self, dashed: Optional[bool] = True) -> int:
        if dashed:
            return super().__str__()
        else:
            return str(super())

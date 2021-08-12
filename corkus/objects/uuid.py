from __future__ import annotations
from typing import Optional
from uuid import UUID

class CorkusUUID(UUID):
    """Simple class that overlays `UUID <https://docs.python.org/3/library/uuid.html>`_ and simplify it's conversion."""
    def __init__(self, uuid: str) -> None:
        super().__init__(uuid)

    def string(self, dashed: Optional[bool] = True) -> str:
        """Convert UUID to dashed or not dashed string

        :param dashed: Should UUID be dashed."""
        if dashed:
            return super().__str__()
        else:
            return str(super().hex)

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corkus import Corkus


class Endpoint():
    def __init__(self, corkus: Corkus) -> None:
        self._corkus = corkus

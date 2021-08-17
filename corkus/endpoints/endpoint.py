from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corkus import Corkus
    from corkus.utils.request import CorkusRequest

class Endpoint():
    def __init__(self, corkus: Corkus, request: CorkusRequest) -> None:
        self._corkus = corkus
        self._request = request

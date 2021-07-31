from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corkus import Corkus

class PartialBase:
    def __init__(self, corkus: Corkus):
        self.corkus = corkus

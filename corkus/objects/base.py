from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corkus import Corkus

class CorkusBase:
    def __init__(self, corkus: Corkus, attributes: dict):
        self.corkus = corkus
        self.attributes = attributes

from __future__ import annotations
from typing import TYPE_CHECKING

from .partial_base import PartialBase

if TYPE_CHECKING:
    from corkus import Corkus

class CorkusBase(PartialBase):
    def __init__(self, corkus: Corkus, attributes: dict):
        super().__init__(corkus)
        self._attributes = attributes

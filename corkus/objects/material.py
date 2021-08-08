from __future__ import annotations
from .base import CorkusBase

class Material(CorkusBase):
    @property
    def name(self) -> str:
        """Name of the material like `Refined Copper Ingot` or `Refined Wheat String`"""
        return self._attributes.get("name", "")

    @property
    def amount(self) -> int:
        """Amount of this material to craft that item"""
        return self._attributes.get("amount", 0)

    def __repr__(self) -> str:
        return f"<Material name={self.name!r} amount={self.amount}>"

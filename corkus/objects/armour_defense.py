from __future__ import annotations

from .base import CorkusBase

class ArmourDefence(CorkusBase):
    """Defence properties of :py:class:`Item`."""
    @property
    def fire(self) -> int:
        """Defence against fire element attacks."""
        return self._attributes.get("fireDefense", 0)

    @property
    def water(self) -> int:
        """Defence against water element attacks."""
        return self._attributes.get("waterDefense", 0)

    @property
    def air(self) -> int:
        """Defence against air element attacks."""
        return self._attributes.get("airDefense", 0)

    @property
    def thunder(self) -> int:
        """Defence against thunder element attacks."""
        return self._attributes.get("thunderDefense", 0)

    @property
    def earth(self) -> int:
        """Defence against earth element attacks."""
        return self._attributes.get("earthDefense", 0)

    def __repr__(self) -> str:
        return (
            f"<ArmourDefence fire={self.fire} water={self.water} "
            f"air={self.air} thunder={self.thunder} earth={self.earth}>"
        )

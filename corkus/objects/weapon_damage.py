from __future__ import annotations
from .base import CorkusBase

class WeaponDamage(CorkusBase):
    """Damage dealt by a weapon."""
    @property
    def neutral(self) -> str:
        """Amount of neutral damage this weapon deals. Format: ``Minimum-Maximum``."""
        return self._attributes.get("damage", "0-0")

    @property
    def fire(self) -> str:
        """Amount of fire damage this weapon deals. Format: ``Minimum-Maximum``."""
        return self._attributes.get("fireDamage", "0-0")

    @property
    def water(self) -> str:
        """Amount of water damage this weapon deals. Format: ``Minimum-Maximum``."""
        return self._attributes.get("waterDamage", "0-0")

    @property
    def air(self) -> str:
        """Amount of air damage this weapon deals. Format: ``Minimum-Maximum``."""
        return self._attributes.get("airDamage", "0-0")

    @property
    def thunder(self) -> str:
        """Amount of thunder damage this weapon deals. Format: ``Minimum-Maximum``."""
        return self._attributes.get("thunderDamage", "0-0")

    @property
    def earth(self) -> str:
        """Amount of earth damage this weapon deals. Format: ``Minimum-Maximum``."""
        return self._attributes.get("earthDamage", "0-0")

    def __repr__(self) -> str:
        return (
            f"<WeaponDamage neutral={self.neutral} fire={self.fire} water={self.water} "
            f"air={self.air} thunder={self.thunder} earth={self.earth}>"
        )

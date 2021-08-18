from __future__ import annotations
from typing import Union, TYPE_CHECKING
from .base import CorkusBase
from .enums import ProfessionType

if TYPE_CHECKING:
    from corkus import Corkus

class PlayerProfession(CorkusBase):
    """Information about :py:class:`Player` progress in a specified profession."""
    def __init__(self, corkus: Corkus, name: str, attributes: dict):
        super().__init__(corkus, attributes)
        self._name = name

    @property
    def name(self) -> str:
        """Pretty name of the profession like ``Alchemism``, ``Mining`` or even ``Combat``"""
        # pylint: disable=no-member
        return self.type.value.capitalize()

    @property
    def type(self) -> ProfessionType:
        """Type of the profession."""
        return ProfessionType(self._name.upper())

    @property
    def level(self) -> int:
        """Current level in profession. This value is minimum of ``1``
        and maximum of ``106`` for combat and ``132`` for other professions."""
        return self._attributes.get("level", 1)

    @property
    def level_progress(self) -> Union[float, None]:
        """Progress to next level in precentage 0-100%

        .. note::
            When a player reach max profession level ``132`` this will insteed
            return ``None`` but player can still collect XP.

            When a player reach combat level ``106`` this may exceed 100%.
        """
        return self._attributes.get("xp", 0)

    def __repr__(self) -> str:
        return f"<PlayerProfession name={self.name!r} level={self.level}>"

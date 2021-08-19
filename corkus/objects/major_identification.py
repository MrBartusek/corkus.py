from __future__ import annotations
from typing import TYPE_CHECKING

from .base import CorkusBase
from corkus.data.major_ids import major_ids

if TYPE_CHECKING:
    from corkus import Corkus

class MajorIdentification(CorkusBase):
    """Major IDs are a type of special :py:class:`Identification` but, they are not
    randomly rolled and they provide a wide range of effects that cannot be acquired
    elsewhere"""
    @property
    def id(self) -> str:
        """The id of the Major ID like ``PLAGUE`` or ``ARCANES``."""
        return self._attributes

    @property
    def name(self) -> str:
        """The name of the Major ID like ``Plague`` or ``Transcendence``."""
        return self._id_data.get("name", "")

    @property
    def effect(self) -> str:
        """The description of effect this Major ID provide."""
        return self._id_data.get("effect", "")

    @property
    def _id_data(self) -> dict:
        return major_ids.get(self.id, {})

    def __repr__(self) -> str:
        return f"<MajorIdentification name={self.name!r}>"

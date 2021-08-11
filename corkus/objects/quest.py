from __future__ import annotations
from .base import CorkusBase

class Quest(CorkusBase):
    """Represents a `Quest <https://wynncraft.fandom.com/wiki/Quests>`_ completed by a :py:class:`Player`"""
    @property
    def name(self) -> str:
        """The name of quest."""
        return self._attributes

    @property
    def mini(self) -> bool:
        """Is this quest a `Mini - Quest <https://wynncraft.fandom.com/wiki/Quests#Mini-Quests>`_."""
        return self.name.startswith("Mini-Quest - ")

    @property
    def wiki_url(self) -> str:
        """URL to the Wynncraft Wiki article about this quest."""
        if self.mini:
            return "https://wynncraft.fandom.com/wiki/Quests#Mini-Quests"
        else:
            return "https://wynncraft.fandom.com/wiki/" + self.name.replace(" ", "_")

    def __repr__(self) -> str:
        return f"<Quest name={self.name!r}>"

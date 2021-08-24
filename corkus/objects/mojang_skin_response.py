from __future__ import annotations
from datetime import datetime
from typing import Union

from .base import CorkusBase
from .uuid import CorkusUUID

class MojangSkinResponse(CorkusBase):
    """Represents a response from Mojang API containing information about minecraft
    player skin. For more information see
    `Mojang documentation <https://wiki.vg/Mojang_API#UUID_to_Profile_and_Skin.2FCape>`_.
    """
    @property
    def requested(self) -> Union[datetime, None]:
        """Datetime when request to Mojang API actually was sent. Note that this property might be missing."""
        if self._attributes.get("timestamp") is not None:
            return datetime.fromtimestamp(self._attributes.get("timestamp", 0) / 1000)
        else:
            return None

    @property
    def uuid(self) -> Union[CorkusUUID, None]:
        """Minecraft UUID of player. Note that this property might be missing."""
        if self._attributes.get("profileId") is not None:
            return CorkusUUID(self._attributes.get("profileId"))
        else:
            return None

    @property
    def username(self) -> Union[str, None]:
        """Minecraft username of player. Note that this property might be missing."""
        return self._attributes.get("profileName")

    @property
    def url(self) -> str:
        """URL to the player's skin."""
        return self._attributes.get("textures", {}).get("SKIN", {}).get("url", "")

    def __repr__(self) -> str:
        return f"<MojangSkinResponse username={self.username!r} skin_url={self.url!r}>"

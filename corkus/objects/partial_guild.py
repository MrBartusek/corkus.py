from .partial_base import PartialBase
from .guild import Guild
from corkus.objects import guild

class PartialGuild(PartialBase):
    def __init__(self, corkus, name: str):
        super().__init__(corkus)
        self.name = name

    async def fetch(self) -> Guild:
        return await self.corkus.guild.get(self.name)

    def __repr__(self) -> str:
        return f"<PartialGuild name={self.name}>"

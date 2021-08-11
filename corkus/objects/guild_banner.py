from __future__ import annotations
from typing import List, Literal
from .base import CorkusBase
from enum import Enum

class BannerColor(Enum):
    """List of colors available for :py:class:`GuildBanner` and :py:class:`GuildBannerLayer`."""
    WHITE = "WHITE"
    ORANGE = "ORANGE"
    MAGENTA = "MAGENTA"
    LIGHT_BLUE = "LIGHT_BLUE"
    YELLOW = "YELLOW"
    LIME = "LIME"
    PINK = "PINK"
    GRAY = "GRAY"
    LIGHT_GRAY = "LIGHT_GRAY"
    CYAN = "CYAN"
    PURPLE = "PURPLE"
    BLUE = "BLUE"
    BROWN = "BROWN"
    GREEN = "GREEN"
    RED = "RED"
    BLACK = "BLACK"

class BannerPattern(Enum):
    """List of patterns available for :py:class:`GuildBannerLayer`."""
    CIRCLE_MIDDLE = "CIRCLE_MIDDLE"
    SQUARE_BOTTOM_LEFT = "SQUARE_BOTTOM_LEFT"
    SQUARE_BOTTOM_RIGHT = "SQUARE_BOTTOM_RIGHT"
    SQUARE_TOP_LEFT = "SQUARE_TOP_LEFT"
    SQUARE_TOP_RIGHT = "SQUARE_TOP_RIGHT"
    HALF_HORIZONTAL = "HALF_HORIZONTAL"
    STRIPE_BOTTOM = "STRIPE_BOTTOM"
    STRIPE_TOP = "STRIPE_TOP"
    HALF_VERTICAL = "HALF_VERTICAL"
    STRIPE_LEFT = "STRIPE_LEFT"
    STRIPE_CENTER = "STRIPE_CENTER"
    STRIPE_RIGHT = "STRIPE_RIGHT"
    STRIPE_MIDDLE = "STRIPE_MIDDLE"
    STRAIGHT_CROSS = "STRAIGHT_CROSS"
    STRIPE_DOWNLEFT = "STRIPE_DOWNLEFT"
    STRIPE_DOWNRIGHT = "STRIPE_DOWNRIGHT"
    CROSS = "CROSS"
    DIAGONAL_LEFT = "DIAGONAL_LEFT"
    DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
    TRIANGLE_TOP = "TRIANGLE_TOP"
    TRIANGLE_BOTTOM = "TRIANGLE_BOTTOM"
    RHOMBUS_MIDDLE = "RHOMBUS_MIDDLE"
    TRIANGLES_TOP = "TRIANGLES_TOP"
    TRIANGLES_BOTTOM = "TRIANGLES_BOTTOM"
    CURLY_BORDER = "CURLY_BORDER"
    BORDER = "BORDER"
    STRIPE_SMALL = "STRIPE_SMALL"
    BRICKS = "BRICKS"
    GRADIENT = "GRADIENT"
    CREEPER = "CREEPER"
    SKULL = "SKULL"
    FLOWER = "FLOWER"
    MOJANG = "MOJANG"
    DIAGONAL_LEFT_MIRROR = "DIAGONAL_LEFT_MIRROR"
    DIAGONAL_RIGHT = "DIAGONAL_RIGHT"
    GRADIENT_UP = "GRADIENT_UP"
    HALF_HORIZONTAL_MIRROR = "HALF_HORIZONTAL_MIRROR"
    HALF_VERTICAL_MIRROR = "HALF_VERTICAL_MIRROR"

class GuildBannerLayer(CorkusBase):
    """Represents a layer of :py:class:`GuildBanner`"""
    @property
    def color(self) -> BannerColor:
        """Color of the pattern."""
        return BannerColor(self._attributes.get("colour", "WHITE"))

    @property
    def pattern(self) -> BannerPattern:
        """Pattern used on that layer."""
        return BannerPattern(self._attributes.get("pattern", "CROSS"))

    def __repr__(self) -> str:
        return f"<GuildBannerLayer color={self.color.value!r} pattern={self.pattern.value!r}>"

class GuildBanner(CorkusBase):
    """:py:class:`Guild` banners are used to showcase a guild by means of a banner whenever
    they control a :py:class:`Territory`. Each banner is exclusive and thus no two guilds can have the same banner."""
    @property
    def base_color(self) -> BannerColor:
        """Color of the banner background."""
        return BannerColor(self._attributes.get("base", "WHITE"))

    @property
    def tier(self) -> Literal[1, 2, 3, 4, 5, 6]:
        """Tier of the banner represented by pedestal."""
        return self._attributes.get("tier", 1)

    @property
    def layers(self) -> List[GuildBannerLayer]:
        """List of banner layers."""
        return [GuildBannerLayer(self._corkus, l) for l in self._attributes.get("layers", {})]

    def __repr__(self) -> str:
        return f"<GuildBanner tier={self.tier} base_color={self.base_color.value!r} layers={self.layers}>"

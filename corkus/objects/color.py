from typing import Tuple

class Color:
    """Represents a color returned by API. This class is similar
    to a (red, green, blue) :py:class:`tuple`.
    """
    def __init__(self, rgb: Tuple[int, int, int]) -> None:
        self._value = rgb

    @property
    def r(self) -> int:
        """Return red component of the color."""
        return self._value[0]

    @property
    def g(self) -> int:
        """Return green component of the color."""
        return self._value[1]

    @property
    def b(self) -> int:
        """Return blue component of the color."""
        return self._value[2]

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """Return (red, green, blue) :py:class:`tuple`"""
        return self._value

    @property
    def hex(self) -> str:
        """Return hex representation of color like ``#4e80f7``."""
        return '#%02x%02x%02x' % self._value

    def __str__(self) -> str:
        return self.hex

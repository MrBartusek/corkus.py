from aiohttp import ClientResponse

class CorkusException(Exception):
    """Base exception class for Corkus.py

    Ideally speaking, this could be caught to handle any exceptions thrown from this library.
    """

class HTTPException(CorkusException):
    """Exception that's thrown when an HTTP request operation fails."""
    def __init__(self, response: ClientResponse) -> None:
        super().__init__()
        self._response = response

    @property
    def response(self) -> ClientResponse:
        """Failed response returned by AIOHTTP

        .. |ClientResponse| replace:: ``ClientResponse``
        .. _ClientResponse: https://docs.aiohttp.org/en/latest/client_reference.html#aiohttp.ClientResponse

        :rtype: |ClientResponse|_"""
        return self._response

class WynncraftServerError(HTTPException):
    """Exception that's thrown for when a 500 range status code occurs.

    This error indicates an unexpected error prevent the server from processing the request.
    If the error continues occurring for the same request it should be reported on the
    `Wynncraft API issue tracker <https://github.com/Wynncraft/WynncraftAPI/issues>`_;
    or if you believe the error is exploitable, or directly to Colin (Colin#0670 on discord, colin350 on the forums)
    if the issue is exploitable/poses a risk to the stability of the API."""

class RatelimitExceeded(HTTPException):
    """Exception that's thrown for when a 429 status code occurs.

    .. warning::

        This exception shouldn't be thrown when using Corkus normally.
        If you see that error it's most likely because you disabled :ref:`ratelimit`.
        If you are sure that rate limit is enabled please
        `create a bug repport <https://github.com/MrBartusek/corkus.py/issues/new>`_

    .. danger::

        IPs that repeatedly exceed the rate limit could be blacklisted.

    """

class BadRequest(HTTPException):
    """Exception that's thrown for when a 400 status code occurs.

    Indicates that a parameter given by the client was in an incorrect format,
    or that the requested resource doesn't exist. This client should not
    immediately request this resource again without changes.

    Common reasons:

    - The requested resource doesn't exists (e.g. The requested username hasn't logged onto Wynncraft when getting player stats; the requested ingredient doesn't exist)
    - A provided argument wasn't in the correct format (for example when searching by level in recipe api, provided a letter instead of a number)
    - When using more advanced search route, an invalid symbol or prop is provided"""

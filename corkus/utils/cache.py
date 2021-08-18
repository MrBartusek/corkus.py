from __future__ import annotations
from typing import List, Union
import time
import logging

logger = logging.getLogger("corkus.cache")

class CacheElement():
    def __init__(
        self,
        endpoint_url: str,
        valid_timestamp: int,
        content: dict
    ) -> None:
        self._url = endpoint_url
        self._valid_timestamp = valid_timestamp
        self._content = content

    @property
    def url(self) -> str:
        return self._url

    @property
    def valid_timestamp(self) -> int:
        return self._valid_timestamp

    @property
    def content(self) -> dict:
        return self._content

    def __repr__(self) -> str:
        return f"<CacheElement url={self.url!r} valid_timestamp={self.valid_timestamp}>"

class CorkusCache:
    def __init__(self) -> None:
        self._cache: List[CacheElement] = []

    @property
    def content(self) -> List[CacheElement]:
        for item in self._cache:
            if item.valid_timestamp <= time.time():
                self._cache.remove(item)
        return self._cache

    def get(self, url: str) -> Union[CacheElement, None]:
        element = next((i for i in self.content if i.url == url), None)
        if element is None:
            logger.debug(f"Not found in cache: {url}")
        else:
            logger.debug(f"Serving from cache: {url}")
        return element

    def add(self, url: str, headers: dict, content: dict) -> None:
        cache_header = headers.get("cache-control", None)
        if cache_header is None:
            logger.debug(f"No cache-control for: {url} - default to 600")
            cache_header = "max-age=600"
        seconds = cache_header.replace("max-age=", "")
        if not seconds.isdigit():
            logger.debug(f"Invalid cache-control ({seconds}) for: {url} - default to 600")
            seconds = 600
        logger.debug(f"Caching: {url} - for {seconds} seconds")

        self._cache.append(CacheElement(url, int(time.time()) + int(seconds), content))

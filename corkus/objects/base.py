from corkus.objects.metadata import CorkusMetadata

class CorkusBase:
    def __init__(self, attributes: dict,  metadata: CorkusMetadata):
        self.attributes = attributes
        self._metadata = metadata

    @property
    def metadata(self) -> CorkusMetadata:
        return self._metadata

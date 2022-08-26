from abc import ABC


class LunarCrushABC(ABC):
    _BASE_URL = ''

    def __init__(self, api_key=None):
        self._api_key = api_key

    def _request(self, endpoint, **kwargs):
        raise NotImplementedError('Request method not implemented')

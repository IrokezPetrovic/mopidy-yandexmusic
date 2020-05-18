from .classes import YMTrack


class YMTrackCache:
    def __init__(self):
        self._cache = dict()

    def put(self, track: YMTrack):
        self._cache[track.uri] = track

    def get(self, uri: str) -> YMTrack:
        if uri not in self._cache:
            return None

        track = self._cache[uri]
        return track

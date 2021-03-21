from mopidy import backend, models
from yandex_music import Client
from .caches import YMTrackCache
from .classes import YMTrack


class YandexMusicLibraryProvider(backend.LibraryProvider):
    def __init__(self, client: Client, track_cache: YMTrackCache):
        self._client = client
        self._track_cache = track_cache
        self.root_directory = models.Ref.directory(uri="yandexmusic:directory:root", name="root")

    def browse(self, uri):
        return None

    def _lookup_album(self, album_id: str):
        album = self._client.albums_with_tracks(album_id=album_id)
        tracks = list()
        for vol in album.volumes:
            ymtracks = list(map(YMTrack.from_track, vol))
            tracks = tracks + ymtracks

        return tracks


    def lookup(self, uri: str):
        parts = uri.split(":")
        if (parts[1] == "album"):
            return self._lookup_album(parts[2])
        track = self._track_cache.get(uri)
        if track is not None:
            return [track]

        _, kind, ymartist_id, ymtrack_id = uri.split(":")
        track_id = f"{ymartist_id}:{ymtrack_id}"
        ymtrack = self._client.tracks(track_id)

        if isinstance(ymtrack, list):
            tracks = list(map(YMTrack.from_track, ymtrack))
            for track in tracks:
                self._track_cache.put(track)
            return tracks
        else:
            track = YMTrack.from_track(ymtrack)
            return [track]

    def get_images(self, uris):
        result = dict()

        for uri in uris:
            _, kind, id = uri.split(":", 2)
            if kind == "track":
                track = self._track_cache.get(uri)
                if track is None:
                    continue
                artwork_uri = "https://" + track.artwork.replace("%%", "400x400")
                result[uri] = [models.Image(uri=artwork_uri)]
            if kind == "playlist":
                pass
        return result

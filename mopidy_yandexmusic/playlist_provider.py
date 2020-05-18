from mopidy import backend
import yandex_music
from .classes import YMRef, YMPlaylist
from typing import List
from .caches import YMTrackCache


class YandexMusicPlaylistProvider(backend.PlaylistsProvider):
    def __init__(self, client: yandex_music.Client, track_cache: YMTrackCache):
        self._client = client
        self._track_cache = track_cache

    def as_list(self) -> List[YMRef]:
        playlists = self._client.users_playlists_list()

        refs = list(map(YMRef.from_playlist, playlists))
        return refs

    def get_items(self, uri: str) -> YMRef:
        _, kind, ym_userid, playlist_id = uri.split(":")

        if ym_userid == str(self._client.me.account.uid):
            playlist = self._client.users_playlists(playlist_id)[0]
            track_ids = list(map(lambda t: t.track_id, playlist.tracks))
            tracks = self._client.tracks(track_ids)
            refs = list(map(YMRef.from_track, tracks))
            return refs

    def lookup(self, uri: str) -> YMPlaylist:
        _, kind, ym_userid, playlist_id = uri.split(":")
        try:
            if ym_userid == str(self._client.me.account.uid):
                ymplaylist = self._client.users_playlists(playlist_id)[0]
                track_ids = list(map(lambda t: t.track_id, ymplaylist.tracks))
                ymplaylist.tracks = self._client.tracks(track_ids)
                playlist = YMPlaylist.from_playlist(ymplaylist)
                for track in playlist.tracks:
                    self._track_cache.put(track)
                return playlist
        except Exception as e:
            print("Exception")

    def create(self, name):
        return None

    def delete(self, uri):
        return None

    def refresh(self):
        pass

    def save(self, playlist):
        return None

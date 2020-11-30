from unittest import TestCase
from yandex_music import Client
import os
_login = os.environ.get("ym_login")
_passwd = os.environ.get("ym_passwd")


class YMClientTests(TestCase):
    def __init__(self, method_name: str):
        super().__init__(method_name)
        self._client = Client.from_credentials(username=_login, password=_passwd)

    def test_get_playlists(self):
        playlists = self._client.users_playlists_list()
        print(playlists)
        tracks = playlists[0].tracks
        print(tracks)

    def test_get_daily(self):
        daily_playlist = self._client.users_playlists_list(user_id="yamusic-origin")
        dd = self._client.users_playlists(kind=daily_playlist[0].kind, user_id="yamusic-origin")
        tracks = dd[0].tracks
        print(tracks)


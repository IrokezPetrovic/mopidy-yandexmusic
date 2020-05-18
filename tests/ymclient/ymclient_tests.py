from unittest import TestCase
from yandex_music import Client

_login = ""
_passwd = ""


class YMClientTests(TestCase):
    def __init__(self, method_name: str):
        super().__init__(method_name)
        self._client = Client.from_credentials(username=_login, password=_passwd)

    def test_get_playlists(self):
        playlists = self._client.users_playlists_list()
        print(playlists)
        tracks = playlists[0].tracks
        print(tracks)

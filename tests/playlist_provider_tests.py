from unittest import TestCase
from test import ymclient
from mopidy_yandexmusic.playlist_provider import YandexMusicPlaylistProvider
from mopidy_yandexmusic.playback_provider import YandexMusicPlaybackProvider
from mopidy_yandexmusic.caches import YMTrackCache


class PlaylistProviderTests(TestCase):
    def test_as_list(self):
        provider = YandexMusicPlaylistProvider(ymclient.client)
        list = provider.as_list()
        print(list)

    def test_get_items(self):
        provider = YandexMusicPlaylistProvider(ymclient.client)
        list = provider.as_list()
        print(list)

        tracks = provider.get_items(list[0].uri)
        print(tracks)

    def test_lookup(self):
        provider = YandexMusicPlaylistProvider(ymclient.client)
        list = provider.as_list()
        print(list)

        playlist = provider.lookup(list[0].uri)
        print(playlist)

    def test_download(self):
        provider = YandexMusicPlaylistProvider(ymclient.client)
        playback = YandexMusicPlaybackProvider(ymclient.client)
        list = provider.as_list()
        print(list)
        track_refs = provider.get_items(list[0].uri)
        download_url = playback.translate_uri(track_refs[0].uri)
        print(download_url)

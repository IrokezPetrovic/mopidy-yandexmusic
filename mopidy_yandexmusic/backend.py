from mopidy import backend, audio
import pykka
import yandex_music
from .playlist_provider import YandexMusicPlaylistProvider
from .playback_provider import YandexMusicPlaybackProvider
from .library_provider import YandexMusicLibraryProvider
from .caches import YMTrackCache


class YandexMusicBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config: dict, audio: audio):
        super().__init__()

        login = config["yandexmusic"]["login"]
        password = config["yandexmusic"]["password"]
        self._config = config
        self._audio = audio

        client = yandex_music.Client.from_credentials(username=login, password=password)
        track_cache = YMTrackCache()

        self.playlists = YandexMusicPlaylistProvider(client, track_cache)
        self.playback = YandexMusicPlaybackProvider(client, audio, self)
        self.library = YandexMusicLibraryProvider(client, track_cache)

        self.uri_schemes = ["yandexmusic"]

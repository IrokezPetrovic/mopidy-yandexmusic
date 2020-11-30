from mopidy import backend, audio
from yandex_music import Client


class YandexMusicPlaybackProvider(backend.PlaybackProvider):
    def __init__(self, client: Client, audio: audio.Audio, backend: backend.Backend, bitrate:int):
        super().__init__(audio, backend)
        self._client = client
        self._bitrate = bitrate

    def translate_uri(self, uri: str):
        _, kind, artist_id, track_id = uri.split(":")
        uid = f"{artist_id}:{track_id}"
        infos = self._client.tracks_download_info(uid, get_direct_links=True)
        for info in infos:
            if info.codec == "mp3" and info.bitrate_in_kbps == self._bitrate:
                link = info.direct_link
                return link
        return None

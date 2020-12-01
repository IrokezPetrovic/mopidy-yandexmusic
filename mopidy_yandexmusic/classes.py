from mopidy.models import Playlist, Track, Ref, fields, Artist
from yandex_music import Playlist as YMPlaylist, Track as YMTrack, Artist as YArtist


class YMRef(Ref):
    @staticmethod
    def from_raw(owner: str, playlist_id: str, title: str):
        uri = f"yandexmusic:playlist:{owner}:{playlist_id}"
        name = title
        ref = YMRef(type=Ref.PLAYLIST, uri=uri, name=name)

        return ref

    @staticmethod
    def from_playlist(playlist: YMPlaylist):
        uri = f"yandexmusic:playlist:{playlist.playlist_id}"
        name = playlist.title
        ref = YMRef(type=Ref.PLAYLIST, uri=uri, name=name)

        return ref

    @staticmethod
    def from_track(track: YMTrack):
        uri = f"yandexmusic:track:{track.track_id}"
        name = track.title
        ref = YMRef(type=Ref.TRACK, uri=uri, name=name)

        return ref


class YMPlaylist(Playlist):
    @staticmethod
    def from_playlist(playlist: YMPlaylist):
        uri = f"yandexmusic:playlist:{playlist.playlist_id}"
        name = playlist.title
        tracks = list(map(YMTrack.from_track, playlist.tracks))
        return YMPlaylist(uri=uri, name=name, tracks=tracks)


class YMTrack(Track):
    @staticmethod
    def from_track(track: YMTrack):
        uri = f"yandexmusic:track:{track.track_id}"
        name = track.title
        length = track.duration_ms
        artists = list(map(YMArtist.from_artist, track.artists))
        artwork = track.cover_uri
        return YMTrack(uri=uri, name=name, length=length, artwork=artwork, artists=artists)

    artwork = fields.String()


class YMArtist(Artist):
    @staticmethod
    def from_artist(artist: YArtist):
        uri = f"yandexmusic:artist:{artist.id}"
        name = artist.name,
        return YMArtist(uri=uri, name=name[0])

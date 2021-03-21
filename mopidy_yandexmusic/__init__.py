from mopidy import ext, config
import pathlib
from .backend import YandexMusicBackend

__version__ = '0.0.7b1'


class Extension(ext.Extension):
    dist_name = "Mopidy-YandexMusic"
    ext_name = "yandexmusic"
    version = __version__

    def get_default_config(self):
        default_config = config.read(pathlib.Path(__file__).parent / "ext.conf")
        return default_config

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["login"] = config.String()
        schema["password"] = config.Secret()
        schema["bitrate"] = config.Integer(optional=True)
        return schema

    def validate_config(self, config):
        return True

    def setup(self, registry):
        registry.add("backend", YandexMusicBackend)

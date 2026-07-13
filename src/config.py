import tomllib
import os
from platformdirs import PlatformDirs
from typing import Any


class Config:
    def __init__(self):
        dirs = PlatformDirs("gusto", "theaihopgg")
        os.makedirs(dirs.user_config_dir, exist_ok=True)
        config_path = os.path.join(dirs.user_config_dir, "config.toml")
        self._data = tomllib.load(open(config_path, "rb"))

    def _get(self, section_name: str, key: str, default: Any = None) -> Any:
        section: dict = self._data.get(section_name, {})
        value = section.get(key, default)
        return value


__all__ = ("Config",)

from typing import override

import toml

from conf_manager.utils.parsers.base_parser import BaseParser


class TomlParser(BaseParser):
    @override
    def _parse(self, payload: str) -> dict:
        return toml.loads(payload)

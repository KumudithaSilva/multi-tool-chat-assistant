import json
import os


class ConfigLoader:
    _config = None

    @classmethod
    def load_config(cls, path: str = "config.json"):
        """
        Load the JSON config file once and store it in memory.
        """
        if cls._config is None:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Config file not found: {path}")
            with open(path, "r", encoding="utf-8") as f:
                cls._config = json.load(f)
        return cls._config

    @classmethod
    def get_shop_info(cls) -> dict:
        """
        Return the shop information from config.
        """
        config = cls.load_config()
        return config.get("shop_info", {})

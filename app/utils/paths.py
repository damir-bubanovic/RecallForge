from pathlib import Path
import sys


def get_base_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS"))

    return Path(__file__).resolve().parents[2]


def get_asset_path(filename: str) -> str:
    return str(get_base_path() / "assets" / filename)
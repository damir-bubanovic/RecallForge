from pathlib import Path
import sys


def get_base_path():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent.parent

    return Path(__file__).resolve().parents[2]


def get_asset_path(filename: str):
    return str(get_base_path() / "assets" / filename)
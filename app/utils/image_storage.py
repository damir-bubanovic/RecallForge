from pathlib import Path
from shutil import copy2
from uuid import uuid4


BASE_DIR = Path(__file__).resolve().parent.parent.parent
IMAGES_DIR = BASE_DIR / "data" / "images"


def copy_image_to_data(source_path: str) -> str:
    source = Path(source_path)

    if not source.exists():
        raise FileNotFoundError("Selected image does not exist.")

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    new_name = f"{uuid4().hex}{source.suffix.lower()}"
    destination = IMAGES_DIR / new_name

    copy2(source, destination)

    return str(destination)


def image_path_exists(image_path: str | None) -> bool:
    if not image_path:
        return False

    return Path(image_path).exists()
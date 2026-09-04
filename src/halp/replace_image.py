from pathlib import Path


def get_current_image(path: Path):
    with path.open("r") as f:
        return f.readline()


def get_new_image(current_image: str, tag: "str"):
    parts = current_image.split(":")
    parts[1] = tag
    return ":".join(parts)


def replace_image(path: Path, new_image):
    with path.open("w") as f:
        f.write(new_image)

from halp.make_url_readable import make_url_readable as make_it_readable
from halp import replace_image as replace_image_functions
import json
from typing import Annotated
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def make_url_readable(url: str):
    print(json.dumps(make_it_readable(url), indent=2))


@app.command()
def replace_image_tag(
    tag: Annotated[str, typer.Option()],
    path: Annotated[
        Path,
        typer.Argument(
            exists=True, file_okay=True, dir_okay=False, writable=True, readable=True
        ),
    ],
):
    current_image = replace_image_functions.get_current_image(path)
    new_image = replace_image_functions.get_new_image(current_image, tag)

    print(f"Current image: {current_image}")
    print(f"New image:     {new_image}")
    replace = typer.confirm("Are you sure you want to replace it?")
    if not replace:
        print("Not replacing")
        raise typer.Abort()

    replace_image_functions.replace_image(path, new_image)


@app.command()
def replace_image(
    image: Annotated[str, typer.Option()],
    path: Annotated[
        Path,
        typer.Argument(
            exists=True, file_okay=True, dir_okay=False, writable=True, readable=True
        ),
    ],
):
    current_image = replace_image_functions.get_current_image(path)
    print(f"Current image: {current_image}")
    print(f"New image:     {image}")
    replace = typer.confirm("Are you sure you want to replace it?")
    if not replace:
        print("Not replacing")
        raise typer.Abort()

    replace_image_functions.replace_image(path, image)


@app.command()
def show_image(
    path: Annotated[
        Path,
        typer.Argument(
            exists=True, file_okay=True, dir_okay=False, writable=True, readable=True
        ),
    ],
):
    current_image = replace_image_functions.get_current_image(path)
    print(f"Current image: {current_image}")


if __name__ == "__main__":
    app()

from halp.make_url_readable import make_url_readable as make_it_readable
import json

import typer

app = typer.Typer()


@app.command()
def make_url_readable(url: str):
    print(json.dumps(make_it_readable(url), indent=2))


@app.command()
def hello():
    print("Hello")


if __name__ == "__main__":
    app()

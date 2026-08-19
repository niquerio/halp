from urllib.parse import urlsplit, parse_qs


def make_url_readable(url: str):
    parts = urlsplit(url)
    result = {
        "base": f"{parts.scheme}://{parts.netloc}{parts.path}",
        "params": parse_qs(parts.query),
    }

    return result

from urllib.parse import urlsplit, parse_qs, quote_plus


def make_url_readable(url: str):
    parts = urlsplit(url)
    result = {
        "base": f"{parts.scheme}://{parts.netloc}{parts.path}",
        "params": parse_qs(parts.query),
    }

    return result


def url_encode_string(string: str):
    return quote_plus(string)

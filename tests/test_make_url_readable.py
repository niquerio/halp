from halp.make_url_readable import make_url_readable
import pytest


def test_make_url_readable():
    assert make_url_readable("http://example.com/place?thing=stuff&thing=other") == {
        "base": "http://example.com/place",
        "params": {"thing": ["stuff", "other"]},
    }


def test_make_url_readable_more_complicated():
    assert make_url_readable(
        "https://api-na.hosted.exlibrisgroup.com/primo/v1/search?disableSplitFacets=true&limit=10&offset=0&q=any%2Ccontains%2Cmusic&qInclude=facet_lang%2Cexact%2Cspa%7C%2C%7Cfacet_topic%2Cexact%2CMusical+Performances&scope=CentralIndex&sort=rank&tab=CentralIndex&vid=01UMICH_INST%3AUMICH"
    ) == {
        "base": "https://api-na.hosted.exlibrisgroup.com/primo/v1/search",
        "params": {
            "disableSplitFacets": ["true"],
            "limit": ["10"],
            "offset": ["0"],
            "q": ["any,contains,music"],
            "qInclude": [
                "facet_lang,exact,spa|,|facet_topic,exact,Musical Performances",
            ],
            "scope": ["CentralIndex"],
            "sort": ["rank"],
            "tab": ["CentralIndex"],
            "vid": ["01UMICH_INST:UMICH"],
        },
    }

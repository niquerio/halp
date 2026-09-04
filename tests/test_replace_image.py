from halp.replace_image import get_current_image, get_new_image, replace_image


def test_get_current_image(tmp_path):
    content = "thing:stuff"
    p = tmp_path / "image.txt"
    p.write_text(content)

    assert get_current_image(p) == content


def test_get_new_image():
    content = "thing:stuff"
    assert get_new_image(content, "what") == "thing:what"


def test_replace_image(tmp_path):
    content = "thing:stuff"
    p = tmp_path / "image.txt"
    p.write_text(content)

    replace_image(p, "blah")
    assert p.read_text() == "blah"

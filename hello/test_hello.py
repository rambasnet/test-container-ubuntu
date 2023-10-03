import hello


def test_hello() -> None:
    assert hello.hello() == 'Hello World!'

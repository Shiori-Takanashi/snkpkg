from _pytest.capture import CaptureFixture
from snkpkg.hello import hello


def test_hello_output(capsys: CaptureFixture[str]) -> None:
    hello("Alice")
    captured = capsys.readouterr()
    assert captured.out.strip() == "こんにちは、Aliceさん。"

import sys

from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from snkpkg.main import main


def test_main_with_arg(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "argv", ["prog", "Bob"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "こんにちは、Bobさん。"

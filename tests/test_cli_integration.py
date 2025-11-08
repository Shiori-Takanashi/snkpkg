import subprocess
import sys
from pathlib import Path


def test_cli_script() -> None:
    root: Path = Path(__file__).parent.parent / "src" / "snkpkg" / "main.py"
    result: subprocess.CompletedProcess[str] = subprocess.run(
        [sys.executable, str(root), "Charlie"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "こんにちは、Charlieさん。"

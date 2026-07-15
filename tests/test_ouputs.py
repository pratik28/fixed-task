import json 
from pathlib import Path

report_path = Path("/environment/report.json")


def test_report_exists():
    """The agent produced a report file."""
    assert report_path.exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert report_path.stat().st_size > 0, "report.json is empty"

def test_schema():
    data = json.loads(report_path.read_text())

    assert set(data.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }

    assert isinstance(data["total_requests"], int)
    assert isinstance(data["unique_ips"], int)
    assert isinstance(data["top_path"], str)

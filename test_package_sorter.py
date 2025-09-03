import pytest
from package_sorter import Package


@pytest.mark.parametrize(
    "width, height, length, mass, expected",
    [
        (100, 100, 50, 10, "STANDARD"),  # Not bulky, not heavy
        (100, 100, 100, 10, "SPECIAL"),  # Bulky by volume (1_000_000)
        (100, 100, 50, 25, "SPECIAL"),  # Heavy
        (100, 100, 100, 25, "REJECTED"),  # Bulky and heavy
    ])
def test_sort_packages(width, height, length, mass, expected):
    assert Package(width, height, length, mass).classify() == expected


def test_invalid_input():
    with pytest.raises(ValueError):
        Package(-1, 100, 100, 10).classify()

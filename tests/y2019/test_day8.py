from y2019.day8 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day8" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data, 3, 2) == 1

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day8" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data, 25, 6) == 1716

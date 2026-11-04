from y2019.day0 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day0" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 1

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day0" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 2

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day0" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 1

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day0" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 2
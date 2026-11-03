from y2019.day1 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_inpu2t():
    input_path = Path(__file__).parents[2] / YEAR / "day1" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 33583

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day1" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 50346

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day1" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 3423279

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day1" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 5132018
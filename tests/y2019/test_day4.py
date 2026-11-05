from y2019.day4 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day4" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 2

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day4" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 481

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day4" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data, False) == 299

def test_part1a_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day4" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve1a(data) == 481

def test_part2a_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day4" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve1a(data, False) == 299
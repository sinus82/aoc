from y2019.day3 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 6

def test_part1_example_1_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "example_1.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 159

def test_part1_example_2_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "example_2.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 135

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 30

def test_part2_example_1_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "example_1.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 610

def test_part2_example_2_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "example_2.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 410

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 855

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day3" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 11238
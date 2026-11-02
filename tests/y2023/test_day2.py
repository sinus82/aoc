from y2023.day2 import solution
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day2" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 8

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day2" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 2286

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day2" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 2061

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day2" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 72596
from y2023.day4 import solution
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day4" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == (13, 30)

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day4" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == (20117, 13768818)

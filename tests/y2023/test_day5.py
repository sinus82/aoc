from y2023.day5 import solution
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day5" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 35

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day5" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve3(data) == 46

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day5" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 662197086

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day5" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve3(data) == 52510809
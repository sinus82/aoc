from y2023.day3 import solution
from pathlib import Path

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day3" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 4361

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day3" / "example.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 467835

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day3" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 532428

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day3" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 84051670
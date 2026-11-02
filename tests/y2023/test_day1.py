from y2023.day1 import solution
from pathlib import Path

def test_part1_example():
    data = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    assert solution.solve(data) == 142

def test_part1_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day1" / "example_p1.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 142
    assert solution.solve1a(data) == 142

def test_part2_example_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day1" / "example_p2.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 281
    assert solution.solve2a(data) == 281
    assert solution.solve2b(data) == 281

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day1" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 55607
    assert solution.solve1a(data) == 55607


def test_part2_real_input():
    input_path = Path(__file__).parents[2] / "y2023" / "day1" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data) == 55291
    assert solution.solve2a(data) == 55291
    assert solution.solve2b(data) == 55291
from y2019.day7 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_1_input():
    input_path = Path(__file__).parents[2] / YEAR / "day7" / "example_1.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 43210

def test_part1_example_2_input():
    input_path = Path(__file__).parents[2] / YEAR / "day7" / "example_2.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 54321

def test_part1_example_3_input():
    input_path = Path(__file__).parents[2] / YEAR / "day7" / "example_3.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 65210

# def test_part2_example_input():
#     input_path = Path(__file__).parents[2] / YEAR / "day7" / "example.txt"
#     data = input_path.read_text(encoding="utf-8").splitlines()

#     assert solution.solve2(data) == 2

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day7" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data) == 21000

# def test_part2_real_input():
#     input_path = Path(__file__).parents[2] / YEAR / "day7" / "input.txt"
#     data = input_path.read_text(encoding="utf-8").splitlines()

#     assert solution.solve2(data) == 2
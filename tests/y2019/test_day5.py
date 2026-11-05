from y2019.day5 import solution
from . import YEAR
from pathlib import Path

def test_part1_example_7_input_10():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_7.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data, 10, 2) == 10

def test_part2_example_1_input_8():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_1.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,8) == 1

def test_part2_example_1_input_2():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_1.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,2) == 0

def test_part2_example_2_input_7():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_2.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,7) == 1

def test_part2_example_2_input_8():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_2.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,8) == 0

def test_part2_example_3_input_8():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_3.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,8) == 1

def test_part2_example_3_input_2():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_3.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,2) == 0

def test_part2_example_4_input_7():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_4.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,7) == 1

def test_part2_example_4_input_8():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_4.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,8) == 0

def test_part2_example_5_input_0():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_5.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,0) == 0

def test_part2_example_5_input_99():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_5.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,99) == 1

def test_part2_example_6_input_0():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_5.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,0) == 0

def test_part2_example_6_input__99():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_5.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,-99) == 1

def test_part2_example_789_input_7():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_789.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,7) == 999

def test_part2_example_789_input_8():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_789.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,8) == 1000

def test_part2_example_789_input_9():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "example_789.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data,9) == 1001

def test_part1_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve(data, 1, 2) == 4887191

def test_part2_real_input():
    input_path = Path(__file__).parents[2] / YEAR / "day5" / "input.txt"
    data = input_path.read_text(encoding="utf-8").splitlines()

    assert solution.solve2(data, 5) == 3419022
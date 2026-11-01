from pathlib import Path

def check_is_engine_part(data: list[str], y: int, x: int, full_check: bool = True) -> bool:
    if full_check and data[y][x] != '.':
        return True
    elif y > 0 and data[y-1][x] != '.':
        return True
    elif y < len(data)-1 and data[y+1][x] != '.':
        return True
    return False

def solve(data: list[str]) -> int:
    total_sum = 0
    y = 0
    for line in data:
        number = 0
        x = 0
        is_engine_part = False
        for c in line:
            if c.isdigit():
                if number == 0 and x > 0:
                    is_engine_part = check_is_engine_part(data, y, x-1)
                number = number * 10 + int(c)
                if not is_engine_part:
                    is_engine_part = check_is_engine_part(data, y, x, False)
            else:
                if number > 0:
                    if is_engine_part or check_is_engine_part(data, y, x):
                        total_sum += number
                    number = 0
                    is_engine_part = False
            x += 1
        if number > 0:
            if is_engine_part or check_is_engine_part(data, y, x-1, False):
                total_sum += number
        y += 1
    return total_sum

def number_from_line(line: str, x: int) -> int:
    number = 0
    while x > 0 and line[x-1].isdigit():
        x -= 1
    while x < len(line) and line[x].isdigit():
        number = number * 10 + int(line[x])
        x += 1
    return number

def solve2(data: list[str]) -> int:
    total_sum = 0
    y = 0
    for line in data:
        x = 0
        for c in line:
            gears_count = 0
            if c == '*':
                number = 1
                if y > 0:
                    if data[y-1][x].isdigit():
                        gears_count += 1
                        number *= number_from_line(data[y-1], x)
                    else:
                        if x>0 and data[y-1][x-1].isdigit():
                            gears_count += 1
                            number *= number_from_line(data[y-1], x-1)
                        if x < len(line)-1 and data[y-1][x+1].isdigit():
                            gears_count += 1
                            number *= number_from_line(data[y-1], x+1)
                    if x > 0 and data[y][x-1].isdigit():
                        gears_count += 1
                        number *= number_from_line(data[y], x-1)
                    if x < len(line)-1 and data[y][x+1].isdigit():
                        gears_count += 1
                        number *= number_from_line(data[y], x+1)
                if y < len(data)-1:
                    if data[y+1][x].isdigit():
                        gears_count += 1
                        number *= number_from_line(data[y+1], x)
                    else:
                        if x>0 and data[y+1][x-1].isdigit():
                            gears_count += 1
                            number *= number_from_line(data[y+1], x-1)
                        if x < len(line)-1 and data[y+1][x+1].isdigit():
                            gears_count += 1
                            number *= number_from_line(data[y+1], x+1)
                if gears_count == 2:
                    total_sum += number
            x += 1
        y += 1

    return total_sum

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print(solve(data))

    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print(solve2(data))
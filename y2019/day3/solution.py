from pathlib import Path
from time import perf_counter

def find_line(data: str) -> tuple[list[tuple[int, ...]], ...]:
    x = 0
    y = 0
    distance = 0
    lines_h = []
    lines_v = []
    for i in data.split(','):
        line_length = int(i[1:])
        if i[0] == 'U':
            lines_v.append((x, y, y+line_length, distance, 'U'))
            y += line_length
            distance += line_length
        elif i[0] == 'D':
            lines_v.append((x, y-line_length, y, distance, 'D'))
            y -= line_length
            distance += line_length
        elif i[0] == 'R':
            lines_h.append((y, x, x+line_length, distance, 'R'))
            x += line_length
            distance += line_length
        else:
            lines_h.append((y, x-line_length, x, distance, 'L'))
            x -= line_length
            distance += line_length
    return (lines_v, lines_h)

def find_min_intersection(lines: tuple[list[tuple[int, ...]], ...], min_distance: int = 1000000000) -> int:
    for l1 in lines[0]:
        if l1[0] < min_distance:
            for l2 in lines[1]:
                if abs(l1[0]) + abs(l2[0]) < min_distance:
                    if l1[0] >= l2[1] and l1[0] <= l2[2] and l2[0] >= l1[1] and l2[0] <= l1[2] and l1[0] != 0 and l2[0] != 0:
                        min_distance = abs(l1[0]) + abs(l2[0])
    return min_distance

def find_min_length_intersection(lines: tuple[list[tuple[int, ...]], ...], min_distance: int = 1000000000) -> int:
    for l1 in lines[0]:
        if l1[3] < min_distance:
            for l2 in lines[1]:
                if abs(l1[3]) + abs(l2[3]) < min_distance:
                    if l1[0] >= l2[1] and l1[0] <= l2[2] and l2[0] >= l1[1] and l2[0] <= l1[2] and l1[0] != 0 and l2[0] != 0:
                        distance = abs(l1[3]) + abs(l2[3])
                        if l1[4] == 'U':
                            distance += abs(abs(l2[0]) - abs(l1[1]))
                        else:
                            distance += abs(abs(l2[0]) - abs(l1[2]))
                        if l2[4] == 'R':
                            distance += abs(abs(l1[0]) - abs(l2[1]))
                        else:
                            distance += abs(abs(l1[0]) - abs(l2[2]))
                        if distance < min_distance:
                            min_distance = distance
    return min_distance

def solve(data: list[str]) -> int:
    l_1 = find_line(data[0])
    l_2 = find_line(data[1])
    result = find_min_intersection((l_1[0], l_2[1]))
    result = find_min_intersection((l_2[0], l_1[1]), result)
    return result

def solve2(data: list[str]) -> int:
    l_1 = find_line(data[0])
    l_2 = find_line(data[1])
    result = find_min_length_intersection((l_1[0], l_2[1]))
    result = find_min_length_intersection((l_2[0], l_1[1]), result)
    return result

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    start = perf_counter()
    print(solve2(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
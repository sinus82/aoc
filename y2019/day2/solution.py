from pathlib import Path
from time import perf_counter

def intcode(code: list[int], ptr1: int, ptr2: int) -> int:
    # print(code)
    code[1] = ptr1
    code[2] = ptr2
    ptr = 0
    while True:
        if code[ptr] == 99:
            break
        if code[ptr] == 1:
            if code[ptr+3] < len(code) and code[ptr+1] < len(code) and code[ptr+2] < len(code):
                code[code[ptr+3]] = code[code[ptr+1]] + code[code[ptr+2]]
        if code[ptr] == 2:
            if code[ptr+3] < len(code) and code[ptr+1] < len(code) and code[ptr+2] < len(code):
                code[code[ptr+3]] = code[code[ptr+1]] * code[code[ptr+2]]
        ptr += 4

    # print(code)
    return code[0]

def solve(data: list[str]) -> int:
    code = list(map(int, data[0].split(',')))
    return intcode(code, 12, 2)

def solve2(data: list[str]) -> int:
    for i in range(0, 100):
        for j in range(0, 100):
            result = intcode(list(map(int, data[0].split(','))), i, j)
            if result == 19690720:
                return 100 * i + j
    return None

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
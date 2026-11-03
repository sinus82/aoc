from pathlib import Path
from time import perf_counter


def solve(data: list[str]) -> int:
    total = 0
    for i in map(int, data):
        total += int(i/3)-2
    return total

def solve2(data: list[str]) -> int:
    total = 0
    for i in map(int, data):
        f = i
        while True:
            f = int(f/3) - 2
            if f <= 0:
                break

            total += f
    return total

if __name__ == "__main__":
    data = Path("example.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    start = perf_counter()
    print(solve2(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
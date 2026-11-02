from pathlib import Path
from time import perf_counter


def solve(data: list[str]) -> int:
    print(data)
    return 0

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
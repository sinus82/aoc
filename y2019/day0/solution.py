from pathlib import Path
from time import perf_counter


def solve(data: list[str]) -> int:
    print(data)
    return len(data)

def solve2(data: list[str]) -> int:
    return 2*len(data)

if __name__ == "__main__":
    data = Path("example.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
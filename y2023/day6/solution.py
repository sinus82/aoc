from pathlib import Path
from time import perf_counter


def solve_(data: list[str]) -> int:
    total = 1
    for race in data:
        win = 0
        
        for t in range (1, int(race[0])):
            speed = t
            if speed * (int(race[0])-t) > int(race[1]):
                win += 1
        total *= win
    return total

def solve(data: list[str]) -> int:
    return solve_(list(zip(data[0].partition(": ")[2].split(), data[1].partition(": ")[2].split())))

def solve2(data: list[str]) -> list[str]:
    return solve_([("".join(data[0].partition(": ")[2].split()), "".join(data[1].partition(": ")[2].split()))])

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
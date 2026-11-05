from pathlib import Path
from time import perf_counter


def solve(data: list[str]) -> int:
    mapp = {}
    for o in data:
        a, b = o.split(')')
        mapp.setdefault(a,[]).append(b)

    to_visit = [(mapp['COM'], 1)]
    total_sum = 0
    while to_visit:
        point, cost = to_visit.pop()
        total_sum += len(point) * cost
        for i in point:
            if mapp.get(i):
                to_visit.append((mapp[i], cost+1))

    return total_sum

def solve2(data: list[str]) -> int:
    mapp = {}
    for o in data:
        a, b = o.split(')')
        mapp.setdefault(b, []).append(a)
    to_visit = [(mapp['YOU'][0], 0), (mapp['SAN'][0], 0)]
    min_path = {}
    while to_visit:
        point, cost = to_visit.pop()
        if point in min_path:
            return min_path[point] + cost
        if point != 'COM':
            to_visit.append((mapp[point][0], cost+1))
        min_path[point] = cost

    return -1

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve2(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
from pathlib import Path
from time import perf_counter
from itertools import groupby

def solve(data: list[str], one_check = True) -> int:
    rangee = list(map(int, data[0].split('-')))
    found = 0
    for i in range((rangee[1]-rangee[0]+1)):
        number_to_check = int(str(rangee[0]+i)[0])
        ok = True
        for c in str(rangee[0]+i):
            if int(c) < number_to_check:
                ok = False
                break
            number_to_check = int(c)
        contain = False
        if ok:
            for x in range(10):
                if str(x)+str(x) in str(rangee[0]+i) and (one_check or str(x)+str(x)+str(x) not in str(rangee[0]+i)):
                    contain = True
            if contain:
                found += 1
    return found

def solve1a(data: list[str], one_check = True) -> int:
    rangee = list(map(int, data[0].split('-')))
    found = 0
    for i in range((rangee[1]-rangee[0]+1)):
        number = str(rangee[0]+i)
        ok = all( a <= b for a, b in zip(number, number[1:]))
        if not ok:
            continue
        
        if one_check:
            if any(size > 1 for size in (len(list(g)) for _, g in groupby(number))):
                found += 1
        elif any(size == 2 for size in (len(list(g)) for _, g in groupby(number))):
            found += 1

    return found


if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    start = perf_counter()
    print(solve1a(data, False))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
from pathlib import Path
from time import perf_counter

def solve(data: list[str], x, y) -> int:
    id = 0
    min_zero = 100000
    result = 0
    while id < len(data[0]):
        layer = data[0][id:id+x*y]
        if min_zero > len(layer.split('0'))-1:
            min_zero = len(layer.split('0'))-1
            result = (len(layer.split('2'))-1)*(len(layer.split('1'))-1)
        id += x*y
    
    return result

def solve2(data: list[str], x, y) -> None:
    for dy in range(y):
        buf = '';
        for dx in range(x):
            ddx = 0
            while dy*x+dx+ddx <= len(data[0]):
                if data[0][dy*x+dx+ddx] != '2':
                    if data[0][dy*x+dx+ddx] == '1':
                        buf += '#'
                    else:
                        buf += ' '
                    break
                ddx += x*y
        print(buf)
    return None

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data, 25, 6))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    start = perf_counter()
    print(solve2(data, 25, 6))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
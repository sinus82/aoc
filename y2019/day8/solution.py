from pathlib import Path
from time import perf_counter
import time

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

def solve3(data: list[str], x, y) -> None:
    loop = 8
    while loop:
        print("\033[2J\033[H")
        for dy in range(y):
            buf = '';
            for dx in range(x):
                ddx = 0
                while dy*x+dx+ddx < len(data[0]):
                    if data[0][(dy*x+ddx+(dx+(8-loop)*5)%x)%len(data[0])] != '2':
                        if data[0][(dy*x+ddx+(dx+(8-loop)*5)%x)%len(data[0])] == '1':
                            buf += '#'
                        else:
                            buf += ' '
                        break
                    ddx += x*y
            print(buf)
        print("\nPress Control^+C")
        loop -= 1
        if loop == 3:
            loop += 5
        time.sleep(1)
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

    # start = perf_counter()
    # print(solve3(data, 25, 6))
    # end = perf_counter()
    # print(f"Execution time: {(end - start) * 1000:.6f} ms")
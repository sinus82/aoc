def solve(data: str) -> int:
    total = 0 
    for x in data.split():
        total += int(x)

    return total

def solve2(data: str) -> int:
    print(int(x) for x in data.split())
    return sum(int(x) for x in data.split())

if __name__ == "__main__":
    solve2("10 20 30 40")
    print(solve("10 20 30 40"))
def solve(data: str) -> int:
    total = 0
    for x in data.split():
        total += int(x)
    return total

if __name__ == "__main__":
    t = """100
    200
    
    -50
    25"""
    print(solve(t))
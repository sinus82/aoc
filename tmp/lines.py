def solve(data: list[str]) -> int:
    print("data[:-1]:", data[-1:])
    return len(data)

if __name__ == "__main__":
    data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    print(solve(data))

    
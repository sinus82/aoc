from pathlib import Path

def solve(data: list[str]) -> int:
    total = 0
    for x in data:
        ss = x.strip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        total += int(ss[0])*10 + int(ss[-1])
        # print(int(x.strip('1234567890')))
    return total

def solve1a(data: list[str]) -> int:
    total = 0
    for line in data:
        digits = [char for char in line if char.isdigit()]
        print("digits:", digits)
        total += int(digits[0] + digits[-1])
    return total

def solve2(data: list[str]) -> int:
    total = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = {str(i): i for i in range(10)}
    values = {word: index for index, word in enumerate(words, start=1)}
    print("digits:", digits)
    print("values:", values)
    values.update(digits)
    print("values:", values)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for line in data:
        first = (len(line)+1, -1)
        last = (-1, -1)
        
        for index, word in enumerate(words, start=1):
            p = line.find(word)
            if p != -1 and p < first[0]:
                    first = p, index
            p = line.rfind(word)
            if p != -1 and p > last[0]:
                    last = p, index
        for index, word in enumerate(numbers):
            p = line.find(word)
            if p != -1 and p < first[0]:
                    first = p, index
            p = line.rfind(word)
            if p != -1 and p > last[0]:
                    last = p, index
    
        # print("line:", line)
        total += 10*first[1] + last[1]
    return total

def solve2a(data: list[str]) -> int:
    total = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = {str(i): i for i in range(10)}
    values = {word: index for index, word in enumerate(words, start=1)}
    # print("digits:", digits)
    # print("values:", values)
    values.update(digits)
    # print("values:", values)
    for line in data:
        first = (len(line)+1, -1)
        last = (-1, -1)
        for word, index in values.items():
            p = line.find(word)
            if p != -1 and p < first[0]:
                    first = p, index
            p = line.rfind(word)
            if p != -1 and p > last[0]:
                    last = p, index
    
        # print("line:", line)
        total += 10*first[1] + last[1]
    return total

def solve2b(data: list[str]) -> int:
    total = 0
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = {str(i): i for i in range(10)}
    values = {word: index for index, word in enumerate(words, start=1)}
    values.update(digits)
    for line in data:
        first = None
        last = None

        for pos in range(len(line)):
            for word, index in values.items():
                 if line.startswith(word, pos):
                    if first is None:
                        first = index
                    last = pos, index
                    break
        # print("line:", line)
        total += 10*first + last[1]
    return total


if __name__ == "__main__":
    # lines = Path("input.txt").read_text(encoding="utf-8").splitlines()
    lines = Path("example_p1.txt").read_text(encoding="utf-8").splitlines()
    print(solve(lines))

    # lines_p2 = Path("example_p2.txt").read_text(encoding="utf-8").splitlines()
    lines_p2 = Path("example_p2.txt").read_text(encoding="utf-8").splitlines()
    print(solve2b(lines_p2))

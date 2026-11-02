from pathlib import Path
from time import perf_counter

def solve(data: list[str]) -> tuple[int, int]:
    total = 0
    # cards_count = [1 for i in range(len(data))]
    cards_count = [1] * len(data)
    # cards_count = [1 for _ in data]
    for card_index, line in enumerate(data):
        all_numbers = line.partition(":")[2]
        numbers = all_numbers.partition("|")
        win_numbers = numbers[0].strip().split()
        card_value = 1
        wins = 0
        for number in numbers[2].strip().split():
            if number in win_numbers:
                wins += 1
                card_value = card_value << 1
                cards_count[card_index+wins] += cards_count[card_index]
        if card_value > 1:
            total += card_value >> 1

    return total, sum(cards_count)

if __name__ == "__main__":
    data = Path("example.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
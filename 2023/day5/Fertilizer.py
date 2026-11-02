from pathlib import Path
from time import perf_counter

def solve(data: list[str]) -> int:
    seeds = list(map(int, data[:1][0].partition(":")[2].strip().split()))
    # print(seeds)
    new_seeds = []
    for line in (line for line in data[2:] if ":" not in line):
        if len(line) == 0:
            seeds += new_seeds
            new_seeds = []
        else:
            to, fromm, r = map(int, line.split())
            remaining_seeds = []
            for seed in seeds:
                if seed >= fromm and seed < fromm + r:
                    new_seeds.append(to + seed-fromm)
                else:
                    remaining_seeds.append(seed)
            seeds = remaining_seeds
    new_seeds += seeds
    # print("seeds", seeds, "new_seeds", new_seeds)
    return min(new_seeds)    

def solve3(data: list[str]) -> int:
    seed_list = list(map(int, data[0].partition(":")[2].strip().split()))
    seeds = [(seed_list[i], seed_list[i] + seed_list[i+1]) for i in range(0, len(seed_list), 2)]
    # print(seeds)
    new_seeds = []
    for line in (line for line in data[2:] if ":" not in line):
        if len(line) == 0:
            seeds += new_seeds
            new_seeds = []
        else:
            to, source_start, length = map(int, line.split())
            from_s = (source_start, source_start + length)
            remaining_seeds = []
            for seed in seeds:
                if seed[0] >= from_s[0] and seed[1] <= from_s[1]:
                    # print(seed, "is inside", from_s)
                    new_seeds.append((to + seed[0]-from_s[0], to - from_s[0] + seed[1]))
                    # print("from_s:", from_s, " to->", to)
                    # print("new_seed", (to + seed[0]-from_s[0], to - from_s[0] + seed[1]))
                elif seed[0] < from_s[0] and seed[1] <= from_s[1] and seed[1] > from_s[0]:
                        # print(seed, "is overlapping left", from_s)
                        new_seeds.append((to, seed[1]-from_s[0]+to))
                        # print("to->", to)
                        # print("new_seed", (to, min(seed[1], from_s[1])))
                        remaining_seeds.append((seed[0], from_s[0]))
                        # print("remaining_seeds", (seed[0], from_s[0]))
                elif seed[0] >= from_s[0] and seed[0] < from_s[1]:
                    # print(seed, "is overlapping right", from_s)
                    new_seeds.append((to+(seed[0]-from_s[0]), to + (from_s[1]-from_s[0])))
                    # print("to->", to)
                    # print("new_seed", (to+(seed[0]-from_s[0]), to + (from_s[1]-from_s[0])))
                    remaining_seeds.append((from_s[1], seed[1]))
                    # print("remaining_seeds", (from_s[1], seed[1]))
                elif seed[0] < from_s[0] and seed[1] > from_s[1]:
                    # print(seed, "is overlapping both", from_s)
                    new_seeds.append((to, to + (from_s[1]-from_s[0])))
                    remaining_seeds.append((seed[0], from_s[0]))
                    remaining_seeds.append((from_s[1], seed[1]))
                else:
                    # print(seed, "is outside", from_s)
                    remaining_seeds.append(seed)
            seeds = remaining_seeds
    new_seeds += seeds
    # print("new_seeds", new_seeds)
    return min(new_seeds)[0]

if __name__ == "__main__":
    data = Path("example.txt").read_text(encoding="utf-8").splitlines()
    start = perf_counter()
    # print(solve(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")

    tart = perf_counter()
    print(solve3(data))
    end = perf_counter()
    print(f"Execution time: {(end - start) * 1000:.6f} ms")
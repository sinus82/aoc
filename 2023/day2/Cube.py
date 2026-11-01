
from pathlib import Path

def solve(lines: list[str]) -> int:
    balls_limit = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total_sum = 0
    for line in lines:
        game_ok = True
        games = line.partition(':')
        for game in games[2].split(";"):
            for balls in game.split(","):
                ball_info = balls.strip().partition(" ")    
                if balls_limit.get(ball_info[2], 0 ) < int(ball_info[0]):
                    game_ok = False
                    break
            if not game_ok:
                break
        if game_ok:
            total_sum += int(games[0].partition(" ")[2])
    return total_sum

def solve2(lines: list[str]) -> int:
    total_sum = 0
    for line in lines:
        balls_count = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        games = line.partition(':')
        for game in games[2].split(";"):
            for balls in game.split(","):
                ball_info = balls.strip().partition(" ")
                balls_count[ball_info[2]] = max(balls_count[ball_info[2]], int(ball_info[0]))

        total_sum += balls_count["red"] * balls_count["green"] * balls_count["blue"]
    return total_sum

if __name__ == "__main__":
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print(solve(data))

    data = Path("input.txt").read_text(encoding="utf-8").splitlines()
    print(solve2(data))
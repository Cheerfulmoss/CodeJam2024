import random
from random import randint

def generate_map(max_x: int, max_y: int, perc_walls: int, perc_people: int):
    board_sample = {(x, y) for x in range(max_x) for y in range(max_y)}
    board = []
    for _ in range(max_y):
        row = []
        for _ in range(max_x):
            row.append("=")
        board.append(row)

    wall_locals = set(random.sample(
        population=sorted(board_sample),
        k=round(max_x * max_y * (perc_walls / 100))
    ))

    for wall in wall_locals:
        board[wall[1]][wall[0]] = "#"
        board_sample.remove(wall)

    people_locals = set(random.sample(
        population=sorted(board_sample),
        k=round((max_x * max_y - len(wall_locals)) * (perc_people / 100))
    ))

    for person in people_locals:
        board[person[1]][person[0]] = "P"
        board_sample.remove(person)

    pat_zero = random.choice(list(people_locals))

    out_board = []
    for row in board:
        out_board.append("".join(row))

    return out_board, pat_zero


if __name__ == "__main__":
    test_cases = [
        (10, 10, 10, 20),
        (10, 10, 50, 10),
        (10, 10, 10, 50),
        (1000, 1000, 60, 10),
        (1500, 1124, 30, 20),
        (1573, 2356, 10, 20),
        (5678, 8765, 50, 10),
        (45, 67, 10, 50),
        (124, 634, 60, 10),
        (1500, 1124, 30, 20),
    ]

    for number, test_case in enumerate(test_cases):
        max_x, max_y, perc_walls, perc_people = test_case
        game_map, pat_zero = generate_map(max_x, max_y, perc_walls, perc_people)
        with open(f"tests/test_case_{number}.txt", "w") as ofile:
            ofile.write(f"{max_x} {max_y} {pat_zero[0]} {pat_zero[1]}\n")
            ofile.write("".join(game_map))
        with open(f"simple/test_case_{number}.txt", "w") as ofile:
            ofile.write(f"{max_x} {max_y} {pat_zero[0]} {pat_zero[1]}\n")
            for line in game_map:
                ofile.write(f"{line}\n")
        print(f"File written! test_case_{number}.txt")

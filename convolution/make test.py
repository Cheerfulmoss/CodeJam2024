import random
from math import floor

TEST_DIR = "tests"
ME_ONES = "simplified"


def convolutions(x: int, y: int, test_num: int):
    perc_bombs = random.randint(25, 75)
    bomb_locals = set()

    total_size = x * y
    bomb_count = round((perc_bombs / 100) * total_size)
    curr_count = 0

    while curr_count < bomb_count:
        bomb_x = random.randint(0, x - 1)
        bomb_y = random.randint(0, y - 1)
        cell = (bomb_x, bomb_y)
        if cell not in bomb_locals:
            bomb_locals.add(cell)
            curr_count += 1

    while True:
        neigh_seed = (random.randint(0, x - 1),
                      random.randint(0, y - 1))
        if neigh_seed not in bomb_locals:
            break

    with open(f"{ME_ONES}/test_case_{test_num}.txt", "w") as ofile:

        while (not (neigh_size := random.randint(3,
                                                 max(3, floor(min(x, y) ** 0.5))
                                                 )) & 1):
            neigh_size = random.randint(3, max(3, floor(min(x, y) ** 0.5)))

        ofile.write(f"{x} {y} {neigh_size}\n\n")
        for x_local in range(x):
            for y_local in range(y):
                cell = (x_local, y_local)
                if cell == neigh_seed:
                    ofile.write("S")
                elif cell not in bomb_locals:
                    ofile.write(random.choice(["G", "D", "s"]))
                else:
                    ofile.write(random.choice(["B", "M", "g"]))
            ofile.write("\n")

    with open(f"{ME_ONES}/test_case_{test_num}.txt", "r") as ifile:
        with open(f"{TEST_DIR}/test_act_{test_num}.txt", "w") as ofile:
            ofile.write(ifile.readline())
            ifile.readline()
            for line in ifile:
                ofile.write(line.strip())
    print(f"File written! test_act_{test_num}.txt")


if __name__ == "__main__":
    test_cases = [
        (10, 10), (20, 20), (30, 30), (1000, 1000), (5000, 5000),
        (100, 20), (30, 400), (123, 987), (15, 21), (10000, 10000)
    ]
    for index, (x, y) in enumerate(test_cases):
        convolutions(x, y, index)

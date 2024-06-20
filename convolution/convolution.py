import numpy as np
from scipy import signal
from math import floor, ceil
import os


# solution

def convolutions_solution(settings: str, field: str):
    lookup = {
        "B": 2,  # 2
        "M": 3,  # 3
        "g": 1  # 1
    }

    max_y, max_x, size = map(int, settings.split(" "))
    bombs = np.zeros((max_y, max_x), np.int64)

    for index, cell in enumerate(field):
        x = index % max_x
        y = index // max_x
        if cell == "S":
            neigh_seed = (x, y)
        bombs[y, x] = lookup.get(cell, 0)

    bound_x_s = neigh_seed[0] - floor(size / 2)
    bound_x_e = neigh_seed[0] + ceil(size / 2)
    bound_y_s = neigh_seed[1] - floor(size / 2)
    bound_y_e = neigh_seed[1] + ceil(size / 2)

    neighborhood = np.zeros((size, size), np.int64)
    for y, arr_val_y in enumerate(range(bound_y_s, bound_y_e)):
        for x, arr_val_x in enumerate(range(bound_x_s, bound_x_e)):
            if 0 <= arr_val_x < max_x and 0 <= arr_val_y < max_y:
                neighborhood[y, x] = 1 if bombs[arr_val_y, arr_val_x] else 0
            else:
                neighborhood[y, x] = 0
    print("------------")
    print(neighborhood)

    weights = signal.convolve(bombs, neighborhood, mode="same")
    return np.sum(weights)


if __name__ == "__main__":
    for index, filename in enumerate(os.listdir("tests")):
        if filename.endswith(".txt") and "output" not in filename:
            with open(f"tests/{filename}", "r") as ifile:
                settings = ifile.readline()
                field = ifile.readline()
            print(filename)
            output = convolutions_solution(settings, field)
            with open(f"tests/test_act_output_{index}.txt", "w") as ofile:
                ofile.write(str(output))
            print(f"Done! {index}")

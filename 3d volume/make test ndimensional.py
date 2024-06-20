from random import randint, choice
from math import floor, ceil
from itertools import product
from time import perf_counter_ns

POINT = tuple[int, ...]


def within_bound(max_dims: POINT, cell: POINT):
    for i in range(len(max_dims)):
        if cell[i] > max_dims[i] - 2 or cell[i] < 1:
            return False
    return True


def add_coords(coord_one: POINT, coord_two: POINT):
    new_coord = [0] * len(coord_one)
    for i in range(len(coord_one)):
        new_coord[i] = coord_one[i] + coord_two[i]
    return tuple(new_coord)


def make(max_dims: POINT):
    dimensions = len(max_dims)
    surr_cells = []

    for i in range(dimensions):
        for x in range(-1, 2):
            cell = [0] * dimensions
            cell[i] = x
            surr_cells.append(
                tuple(cell)
            )

    total_volume = 1
    for dim in max_dims:
        total_volume *= dim

    bound_one = total_volume ** 0.5
    bound_two = total_volume / 2

    vol_min = floor(min(bound_one, bound_two))
    vol_max = ceil(max(bound_one, bound_two))

    shape_volume = randint(vol_min, vol_max)

    root_cell = [0] * dimensions

    for i in range(dimensions):
        root_cell[i] = randint(1, max_dims[i] - 2)
    root_cell = tuple(root_cell)

    stack = {root_cell}
    in_shape = set()

    while stack and len(in_shape) < shape_volume:
        cell = stack.pop()

        if cell not in in_shape and within_bound(max_dims, cell):
            in_shape.add(cell)

            for surr_cell in surr_cells:
                new_cell = add_coords(cell, surr_cell)
                if within_bound(max_dims, new_cell):
                    stack.add(new_cell)

    border_cells = set()

    for cell in in_shape:
        for surr_cell in surr_cells:
            new_cell = add_coords(cell, surr_cell)

            if new_cell not in in_shape:
                border_cells.add(new_cell)

    return len(in_shape), border_cells, choice(list(in_shape))


def write(in_shape: int, border_cells: set[POINT], root_cell: POINT,
          dimensions: POINT, index: int):
    with open(f"tests/test_case_{index}.txt", "w") as ofile:
        ofile.write(" ".join(map(str, dimensions)))
        ofile.write(f" {root_cell}")
        ofile.write("\n")

        range_dims = [range(max_dim) for max_dim in dimensions]
        dims = len(dimensions)
        prev = None
        curr = None

        for point in product(*range_dims):
            curr = point
            if curr is not None and prev is not None:
                for dim in range(dims):
                    if curr[dim] < prev[dim]:
                        ofile.write("|")

            if point in border_cells:
                ofile.write("#")
            else:
                ofile.write(" ")
            prev = curr

    with open(f"tests/test_case_output_{index}.txt", "w") as ofile:
        ofile.write(str(in_shape))


if __name__ == "__main__":
    test_cases = [
        (4, 4, 4)
    ]
    for index, test_case in enumerate(test_cases):
        print("----------------------")
        print(f"Starting test case {index} generation")
        cumm_start = perf_counter_ns()
        in_shape, border_cells, root_cell = make(test_case)
        make_end = round((perf_counter_ns() - cumm_start) / 10 ** 6, 3)
        print(f"Test made! {make_end:,} ms")
        print("Writing to file!")
        write(in_shape, border_cells, root_cell, test_case, index)
        write_end = round((perf_counter_ns() - cumm_start) / 10 ** 6, 3)
        print(f"Test Written to file! {write_end:,} ms")
        print(f"Finished test case {index} generation")

"""
Question premise.

There is a 3D shape, you need too find it's volume, it's not uniform and kind
of randomly generated.

This is so fuckin cool
"""

import os
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


def flatten_dimension(cell: POINT, dimensions: POINT) -> int:
    flattened = 0
    for i in range(len(cell)):
        flattened *= dimensions[i]
        flattened += cell[i]

    return flattened


def n_volume(details: str, shape: str):
    dims, root = details.strip().split(" (")
    dimensions = len(dims)

    shape = shape.replace("|", "")
    dims = tuple(map(int, dims.split(" ")))
    root = root.replace(",", "").replace("(", "").replace(")", "")
    root = tuple(map(int, root.split(" ")))

    surr_cells = []

    for i in range(dimensions):
        for x in range(-1, 2):
            cell = [0] * dimensions
            cell[i] = x
            surr_cells.append(
                tuple(cell)
            )

    volume_cells = set()
    stack = {root}

    while stack:
        cell = stack.pop()
        flattened = flatten_dimension(cell, dims)

        if cell not in volume_cells and shape[flattened] != "#":
            volume_cells.add(cell)

            for surr_cell in surr_cells:
                new_cell = add_coords(cell, surr_cell)
                if within_bound(dims, new_cell):
                    stack.add(new_cell)

    return len(volume_cells)


if __name__ == "__main__":
    for index, filename in enumerate(os.listdir("tests")):
        if filename.endswith(".txt") and "output" not in filename:
            with open(f"tests/{filename}", "r") as ifile:
                details = ifile.readline()
                shape = ifile.readline()

            print(f"{filename}")
            start = perf_counter_ns()
            print(n_volume(details, shape))
            stop = perf_counter_ns()
            duration = round((stop - start) / 1_000_000, 3)
            print(f"Duration (ms): {duration}")
            print()

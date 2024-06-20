import os
from time import perf_counter_ns


# Solution

def flood(settings: str, region: str):
    max_x, max_y, pat_x, pat_y = map(int, settings.split(" "))
    patient_zero = (pat_x, pat_y)

    stack = {patient_zero}
    found_people = set()
    searched = set()

    while stack:
        x, y = stack.pop()
        cell = (x, y)

        if cell not in searched and region[y * max_x + x] != "#":
            if region[y * max_x + x] == "P" and cell not in found_people:
                found_people.add(cell)

            if x > 0:
                stack.add((x - 1, y))
            if x < max_x - 1:
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < max_y - 1:
                stack.add((x, y + 1))
            searched.add(cell)

    return found_people


if __name__ == "__main__":
    for index, filename in enumerate(os.listdir("tests")):
        if "output" in filename or not filename.endswith(".txt"):
            continue

        print(f"---------------\n{filename}")
        with open(f"tests/{filename}", "r") as ifile:
            settings = ifile.readline()
            region = ifile.readline()

        start = perf_counter_ns()
        output = flood(settings, region)
        stop = perf_counter_ns()
        with open(f"tests/test_case_output_{index}.txt", "w") as ofile:
            ofile.write(str(len(output)))

        print(output)

import random
import string


def node_name(k: int, start: str | None):
    while (
            (node := "".join(random.choices(string.ascii_lowercase, k=k))) ==
            start):
        continue
    return node


def make_maze(path_length: int, id_length: int, index: int):
    path = "".join(random.choices(["U", "D", "L", "R"],
                                  k=path_length))
    maze = {}

    start = node_name(id_length, None)
    fpath = [start]
    used_nodes = {start}
    dummy_nodes = set()

    maze[start] = {
        "U": node_name(id_length, start),
        "D": node_name(id_length, start),
        "L": node_name(id_length, start),
        "R": node_name(id_length, start),
    }

    curr_pos = start
    for dire in path:
        used_nodes.add(maze[curr_pos][dire])
        fpath.append(maze[curr_pos][dire])
        dummies = set(maze[curr_pos].values())
        curr_pos = maze[curr_pos][dire]

        dummy_nodes = dummy_nodes.union(dummies - {curr_pos})

        if curr_pos in maze:
            continue

        maze[curr_pos] = {
            "U": node_name(id_length, start),
            "D": node_name(id_length, start),
            "L": node_name(id_length, start),
            "R": node_name(id_length, start),
        }

    used_dummies = set()
    counter = 0
    while dummy_nodes and counter < path_length * 10:
        # print(len(dummy_nodes))
        dummy = dummy_nodes.pop()
        if dummy in used_nodes or dummy in used_dummies:
            continue
        used_dummies.add(dummy)

        up = node_name(id_length, start)
        down = node_name(id_length, start)
        left = node_name(id_length, start)
        right = node_name(id_length, start)
        maze[dummy] = {
            "U": up,
            "D": down,
            "L": left,
            "R": right,
        }

        if up not in used_dummies and up not in used_nodes:
            dummy_nodes.add(up)

        if down not in used_dummies and down not in used_nodes:
            dummy_nodes.add(down)

        if left not in used_dummies and left not in used_nodes:
            dummy_nodes.add(left)

        if right not in used_dummies and right not in used_nodes:
            dummy_nodes.add(right)

        counter += 1

    ffile = list(maze.keys())
    ffile_len = len(ffile)
    random.shuffle(ffile)

    with open(f"tests/test_case_{index}.txt", "w") as ofile:
        ofile.write(f"Start: {start}\n")
        ofile.write(f"{path}\n")
        for findex, node in enumerate(ffile):
            dirs = maze[node]
            if findex == ffile_len - 1:
                ofile.write(f"{node} || {dirs['U']} {dirs['D']} {dirs['R']} "
                            f"{dirs['L']}")
            else:
                ofile.write(f"{node} || {dirs['U']} {dirs['D']} {dirs['R']} "
                            f"{dirs['L']}, ")

    with open(f"tests/test_case_output_{index}.txt", "w") as ofile:
        ofile.write(curr_pos)

    print("--------------------------")
    print(fpath)
    for i in range(len(fpath)):
        if i == 0:
            continue

        curr = fpath[i - 1]
        next = fpath[i]

        if next not in maze[curr].values():
            print(f"{curr=} {next=} {maze[curr]=}")
            raise ValueError("WTF")


if __name__ == "__main__":
    test_cases = [
        (10, 2), (10, 3), (69, 5), (420, 6), (37, 4), (1000, 4),
        (10000, 5), (56897, 6), (100000, 8)
    ]
    for index, (path_len, id_len) in enumerate(test_cases):
        make_maze(path_len, id_len, index)

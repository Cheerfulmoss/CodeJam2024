import os


def mouse(start: str, path: str, maze: str):
    maze_struct = {}
    cross_roads = maze.split(", ")

    for cross_road in cross_roads:
        if not cross_road:
            continue
        node, dirs = cross_road.split(" || ")
        up, down, right, left = map(str.strip, dirs.split(" "))

        maze_struct[node.strip()] = {
            "U": up,
            "D": down,
            "R": right,
            "L": left,
        }

    fpath = [start]
    curr_node = start
    for dire in path:
        try:
            curr_node = maze_struct[curr_node][dire]
        except KeyError as e:
            print(fpath)
            raise ValueError(e)
        fpath.append(curr_node)

    print(fpath)
    return curr_node


if __name__ == "__main__":
    for filename in os.listdir("tests"):
        if filename.endswith(".txt") and "output" not in filename:
            with open(f"tests/{filename}", "r") as ifile:
                start = ifile.readline().split(": ")[1].strip()
                path = ifile.readline().strip()
                maze = ifile.readline().strip()

            print(f"------------------\n{filename}")
            print(mouse(start, path, maze))


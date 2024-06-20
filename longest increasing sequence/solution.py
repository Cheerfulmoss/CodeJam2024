import os


def solution(details: str, sequence: str):
    number_sequence = map(int, sequence.split(" "))
    return len(set(number_sequence))


if __name__ == "__main__":
    for index, filename in enumerate(os.listdir("tests")):
        if filename.endswith(".txt") and "output" not in filename:
            print(f"{filename} Doing the thing")
            with open(f"tests/{filename}", "r") as ifile:
                ifile.readline()
                sequence = ifile.readline()

            with open(f"tests/test_case_output_{index}.txt", "w") as ofile:
                ofile.write(str(solution("", sequence)))

import random
from random import randint


def sequences(numbers: int, min_number: int, max_number: int):
    return list(random.choices(range(min_number, max_number + 1), k=numbers))


def write_tests():
    test_cases = [
        10, 15, 1000, 1_000_000, 12456, 6_242_456
    ]

    for number, numbers in enumerate(test_cases):
        with open(f"tests/test_case_{number}.txt", "w") as ofile:
            minn = randint(0, (numbers + 1) // 2)
            maxn = randint(minn + 1, numbers + 1)
            out = " ".join(map(str, sequences(numbers, minn, maxn)))
            ofile.write(f"{numbers}\n")
            ofile.write(out)


if __name__ == "__main__":
    write_tests()

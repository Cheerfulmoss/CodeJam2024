from string import ascii_letters
import os


# Solution

def decrypt(encrypted_string: str) -> str:
    chars = encrypted_string.split(" ")
    decrypted_string = []
    for char in chars:
        ascii_code = 0
        for sub_char in char:
            ascii_code += ascii_letters.index(sub_char) + 1
        decrypted_string.append(chr(ascii_code))

    return "".join(decrypted_string)


if __name__ == "__main__":
    for filename in os.listdir("tests"):
        if filename.endswith(".txt") and "output" not in filename:
            with open(f"tests/{filename}") as ifile:
                message = ifile.readline()
            print("--------------------")
            print(filename)
            print(decrypt(message))

    print(decrypt("Zm ZYm ZYm ZS ZU ZYd ZYb ZYg ZY F ZYl ZW ZU ZYm ZYh ZYk F ZJ S X Za T"))

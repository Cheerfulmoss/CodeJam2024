import string
from string import ascii_letters


# solution

def to_alien(sentence: str):
    alien_sentence = []
    for char in sentence:
        letter = []
        value = ord(char)
        for x in range(len(ascii_letters) - 1, -1, -1):
            alien_value = ascii_letters[x]
            x += 1
            if x <= value:
                letter.append(alien_value)
                value -= x
        alien_sentence.append("".join(letter))

    return " ".join(alien_sentence)


if __name__ == "__main__":

    test_cases = [
        "+++ INITIATE NEURAL ENCRYPTION +++ PROCESSING... CONNECTION "
        "ESTABLISHED.",

        "Hostile entities detected in orbital resonance chamber. All units, "
        "commence gravitational inversion protocols.",

        "+++ CANNOT PARSE ENTITY DESIGNATION +++ UNKNOWN ENTITIES ENGAGING "
        "NEURAL NETWORKS.",

        "Biological anomalies detected in quantum field; recommend quarantine "
        "protocols. Over.",

        "Extraterrestrial vessels converging on primary command node. "
        "Initiating hyperdimensional blockade.",

        "Transmission interference detected. Recommend phase-shift modulation "
        "to bypass jamming frequencies.",

        "++ ENEMY COUNTERMEASURES ACTIVATED ++ ALERT! INCOMING NEUTRON FLUX "
        "DETECTED!",

        "Unknown life signatures detected in subspace. All containment teams, "
        "prepare for dimensional lockdown!",

        "+++ CODEX OVERRIDE IMMINENT +++ BRACE FOR TEMPORAL DISRUPTION! "
        "INITIATE TEMPORAL STASIS FIELD!",

        "DANGER: Singularity breach in containment sector ALPHA-7! All "
        "evacuation routes compromised. Repeat, compromised."
        
        "",

        "[TEST] Case: Brackets and other punctuation {}[]<>,./?;':\"|\\`~"
        "!@#$%^&*()_+-="
    ]

    for number, test_case in enumerate(test_cases):
        with open(f"tests/test_case_{number}.txt", "w") as ofile:
            ofile.write(to_alien(test_case))

        with open(f"tests/test_case_output_{number}.txt", "w") as ofile:
            ofile.write(test_case)

    print(to_alien("Attacking sector X-25."))

"""Small educational substitute for selected CrypTool 2 components.

This file is explicitly not CrypTool evidence. It uses only synthetic text and
is retained so a reviewer can reproduce the supplemental observations.
"""

from collections import Counter
import hashlib


def caesar(text, shift):
    out = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            out.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            out.append(char)
    return "".join(out)


def square_for(key):
    chars = []
    for char in (key.upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        char = "I" if char == "J" else char
        if char.isalpha() and char not in chars:
            chars.append(char)
    return [chars[index:index + 5] for index in range(0, 25, 5)]


def playfair_pairs(text):
    letters = ["I" if char == "J" else char for char in text.upper() if char.isalpha()]
    pairs = []
    index = 0
    while index < len(letters):
        first = letters[index]
        second = letters[index + 1] if index + 1 < len(letters) else "X"
        if first == second:
            pairs.append((first, "X"))
            index += 1
        else:
            pairs.append((first, second))
            index += 2
    return pairs


def playfair_encrypt(text, key):
    square = square_for(key)
    positions = {char: (row, column) for row, line in enumerate(square) for column, char in enumerate(line)}
    result = []
    for first, second in playfair_pairs(text):
        row_a, col_a = positions[first]
        row_b, col_b = positions[second]
        if row_a == row_b:
            result.extend((square[row_a][(col_a + 1) % 5], square[row_b][(col_b + 1) % 5]))
        elif col_a == col_b:
            result.extend((square[(row_a + 1) % 5][col_a], square[(row_b + 1) % 5][col_b]))
        else:
            result.extend((square[row_a][col_b], square[row_b][col_a]))
    return "".join(result)


sample = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
caesar_ciphertext = caesar(sample, 3)
counts = Counter(char for char in caesar_ciphertext.upper() if char.isalpha())
print("supplemental_tool=python-standard-library")
print("sample_plaintext=", sample)
print("caesar_shift=3")
print("caesar_ciphertext=", caesar_ciphertext)
print("caesar_round_trip=", caesar(caesar_ciphertext, -3))
print("frequency_top5=", counts.most_common(5))
print("playfair_key=MONARCHY")
print("playfair_plaintext=INSTRUMENTS")
print("playfair_ciphertext=", playfair_encrypt("INSTRUMENTS", "MONARCHY"))
for algorithm in ("md5", "sha256"):
    digest = hashlib.new(algorithm, sample.encode("utf-8")).hexdigest()
    print(f"{algorithm}=", digest)

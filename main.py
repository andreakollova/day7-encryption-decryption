alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
text = input("Type your message:")
shift = input("Type the shift number:")


def encrypt(text, shift):
    index_to_letter = ""
    for letter in text:
        moved_letter = alphabet.index(letter) + int(shift)
        moved_letter = moved_letter % len(alphabet)
        index_to_letter += alphabet[moved_letter]
    print(index_to_letter)


encrypt(text, shift)
CIPHER_DICT = {'a': 'u', 'b': 'd', 'c': 'k', 'd': 'q', 'e': 't', 'f': 'w',
               'g': 'z', 'h': 'b', 'i': 'p', 'j': 'a', 'k': 'e', 'l': 'g',
               'm': 's', 'n': 'm', 'o': 'y', 'p': 'j', 'q': 'h', 'r': 'c',
               's': 'l', 't': 'o', 'u': 'n', 'v': 'v', 'w': 'x', 'x': 'f',
               'y': 'i', 'z': 'r'}


def create_reversed_dict():
    reversed_dict = {}

    for char in CIPHER_DICT:
        reversed_dict[CIPHER_DICT[char]] = char

    return reversed_dict


def decode(decoded_text):
    reversed_dict = create_reversed_dict()

    result = ""

    for char in decoded_text:
        if char in reversed_dict:

            result += reversed_dict[char]

        else:
            result += char

    return result


def encode(encode_text):
    result = ""

    for char in encode_text:
        if char in CIPHER_DICT:
            result += CIPHER_DICT[char]
        else:
            result += char

    return result

print(decode("p us obpmepmz yw ztoopmz u bupckno"))
"""
Module for encoding and decoding strings,
reading IBANS from JSON, and validating them
with a TransactionManager.
"""
import string
from UC3MMoney.TransactionManager import TransactionManager


#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def encode(word):
    """
    Encodes a string using a shift cipher.

    :param word: the string to encode
    :return: the encoded string
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def decode(word):
    """
    Decodes a string that was encoded

    :param word: The encoded string to decode
    :return: the decoded string
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded


def main():
    """
    Main function that reads IBAN from JSON file using
    a TransactionManager, validates the IBAN, encodes and
    decodes the IBAN, and prints the original, encoded, and
    decoded strings.
    """

    mng = TransactionManager()
    res = mng.read_product_code_from_json("test.json")
    str_res = res.__str__()
    print(str_res)
    validate_iban = mng.validate_iban(str_res)
    print(validate_iban)
    encode_res = encode(str_res)
    print("Encoded Res "+ encode_res)
    decode_res = decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("IBAN_FROM: " + res.iban_from)
    print("IBAN_TO: " + res.iban_to)

if __name__ == "__main__":
    main()
    #"from": "ES9121000418450200051332",
    #"to": "ES2400491500162128195151",
    #"receptor_name": "Greta Leege"

#"ES10000010012345678900"
#"ES2400491500162128195151",

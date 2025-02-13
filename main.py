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

def run_test_cases(test_case):
    """
    Function that reads IBAN from JSON file using
    a TransactionManager, validates the IBAN, encodes and
    decodes the IBAN, and prints the original, encoded, and
    decoded strings.
    """

    mng = TransactionManager()
    res = mng.read_product_code_from_json(test_case)

    if mng.validate_iban(res.iban_to) and mng.validate_iban(res.iban_from):
        str_res = res.__str__()
        encode_res = encode(str_res)
        print("Encoded Res " + encode_res)
        decode_res = decode(encode_res)
        print("Decoded Res: " + decode_res)
        print("IBAN_FROM: " + res.iban_from)
        print("IBAN_TO: " + res.iban_to)
    else:
        print("IBAN VALIDATION FAILED")

def main():
    """
    Main function that reads the test files
    """

    print("Valid Iban Test Case: ")
    run_test_cases("CorrectTest.json")

    print("Invalid IBAN Test Case: ")
    run_test_cases("IncorrectTest.json")

if __name__ == "__main__":
    main()




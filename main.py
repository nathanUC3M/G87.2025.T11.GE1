"""

"""
from UC3MMoney.TransactionManager import TransactionManager
import string

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3


def encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) + shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) - shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded


def main():

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

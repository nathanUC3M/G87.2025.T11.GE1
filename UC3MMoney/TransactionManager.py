"""
Transaction Manager

This module defines the Transaction Manager class. This class provides methods
to validate IBANs and process transaction requests from JSON files.
"""
import re
import json
from UC3MMoney.TransactionManagementException import TransactionManagementException
from UC3MMoney.TransactionRequest import TransactionRequest


class TransactionManager:
    """
    A class to manage transaction requests from JSON files.

    Methods: validate_iban(self, iban): Validates the IBAN number based on
    format and digit checking
    read_product_code_from_json(fi): Reads transaction details from a JSON file
    and validates IBANS
    """
    def __init__(self):
        """ Initializes the Transaction Manager class."""


    def validate_iban(self, iban):
        """
        Validates the IBAN, checks if the IBAN has the correct format and
        passes MOD-97 validation

        :param iban (str): The IBAN number to be validated
        :return: bool: True if the IBAN has the correct format and is valid, else false
        """
        iban = iban.replace(" ", "").upper()
        iban_format = re.compile(r"^ES\d{2}[A-Z0-9]+$")

        #Below makes sure parameter matches the IBAN format
        if not iban_format.match(iban):
            return False
        #Moves the values at the indexes 0-3 to the back of the IBAN
        mixed_iban = iban[4:] + iban[:4]
        #Iterates over the IBAN changing the LETTERS to their numeric counterpart
        #according to the ASCII relation
        numeric_iban = "".join(str(ord(char) - 55) if char.isalpha() else char for char in mixed_iban)

        #Converts the IBAN to an integer and performs the MOD 97 on it
        iban_int = int(numeric_iban)
        return iban_int % 97 == 1


    def read_product_code_from_json(self, fi):
        """
        Reads transaction details from a JSON file
        :param fi: (str) The path to the file to be read
        :return: TransactionRequest: An object containing the transaction details
        if the file is valid
        :raises: TransactionManagementException: If the file is not valid or not found
        """

        try:
            with open(fi, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise TransactionManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise TransactionManagementException("JSON decode Error - Wrong JSON Format") from e


        try:
            t_from = data["from"]
            t_to = data["to"]
            to_name = data["receptor_name"]
            req = TransactionRequest(t_from, t_to,to_name)
        except KeyError as e:
            raise TransactionManagementException("JSON decode Error - Invalid JSON Key") from e
        if not self.validate_iban(t_from) :
            raise TransactionManagementException("Invalid FROM IBAN")
        if not self.validate_iban(t_to):
            raise TransactionManagementException("Invalid TO IBAN")
        return req

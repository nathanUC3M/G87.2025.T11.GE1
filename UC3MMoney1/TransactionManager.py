import json
from UC3MMoney1.TransactionManagementException import TransactionManagementException
from TransactionRequest import TransactionRequest
import re


class TransactionManager:
    def __init__(self):
        pass


    def ValidateIBAN( self, IbAn ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        IBAN_FORMAT = re.compile(r"^[A-Z]{2}\d{2}[A-Z0-9]+$")

        if not IBAN_FORMAT.match(IbAn):
            return False

        country_abrv = IbAn[:2]
        if country_abrv != "ES" or country_abrv.isNumeric():
            return False

        mixed_iban = IbAn[4:] + IbAn[:4]
        numeric_iban = "".join(str(ord(char) - 55) if char.isalpha() else char for char in mixed_iban)

        iban_int = int(numeric_iban)
        return iban_int % 97 == 1



    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise TransactionManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise TransactionManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            T_FROM = DATA["from"]
            T_TO = DATA["to"]
            TO_NAME = DATA["receptor_name"]
            req = TransactionRequest(T_FROM, T_TO,TO_NAME)
        except KeyError as e:
            raise TransactionManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateIBAN(T_FROM) :
            raise TransactionManagementException("Invalid FROM IBAN")
        else:
            if not self.ValidateIBAN(T_TO):
                raise TransactionManagementException("Invalid TO IBAN")
        return req
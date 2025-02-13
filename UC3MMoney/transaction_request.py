"""
Transaction Request

This module defines the Transaction Request class. This class provides methods
that requests and holds information about the transaction request
"""
import json
from datetime import datetime

class TransactionRequest:
    """
    Class TransactionRequest

    Represents a transaction request and holds information about a transaction,
    this information includes the IBAN of the receptor's name and a timestamp

    Attributes:
        receptor_name (string): the name of the receptor
        iban_from (string): the IBAN of the sender
        iban_to (string): the IBAN of the receiver
        time_stamp (float): the timestamp of when the transaction was received
    """
    def __init__(self, iban_from, iban_to, receptor_name):
        """
        Initialises a TransactionRequest object.

        :param iban_from (string): the IBAN of the sender
        :param iban_to (string): the IBAN of the receiver
        :param receptor_name (string): the name of the receptor
        """
        self.__receptor_name = receptor_name
        self.__iban_from = iban_from
        self.__iban_to = iban_to
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: string: A JSON string of the TransactionRequest object.
        """
        return "TransactionRequest:" + json.dumps(self.__dict__)

    @property
    def receptor_name(self):
        """
        Gets the receptor name.

        :return: string: The receptor name.
        """
        return self.__receptor_name
    @receptor_name.setter
    def receptor_name(self, value):
        """
        Sets the receptor name.

        :param value (string): the receptor name.
        """
        self.__receptor_name = value

    @property
    def iban_from(self):
        """
        Gets the IBAN of the sender.

        :return: string: The IBAN of the sender.
        """
        return self.__iban_from
    @iban_from.setter
    def iban_from(self, value):
        """
        Sets the IBAN of the sender.
        :param value (string): the IBAN of the sender.
        """
        self.__iban_from = value

    @property
    def iban_to(self):
        """
        Gets the IBAN of the receiver.

        :return: string: The IBAN of the receiver.
        """
        return self.__iban_to
    @iban_to.setter
    def iban_to(self, value):
        """
        Sets the IBAN of the receiver.

        :param value (string): the IBAN of the receiver.
        :return:
        """
        self.__iban_to = value

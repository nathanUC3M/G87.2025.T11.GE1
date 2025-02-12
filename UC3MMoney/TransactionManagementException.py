"""
Transaction Management Exception

This module defines the TransactionManagementException class, that
handles errors in the TransactionManagement class
"""
class TransactionManagementException(Exception):
    """
    Exception class for TransactionManagementException

    parameters:
        Exception: message(string)-- the error message
    """
    def __init__(self, message):
        """
        Initialize the exception with a message
        :param message: description of the exception
        """
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """
        Gets the exception message

        :return: the error message
        """
        return self.__message

    @message.setter
    def message(self,value):
        """
        Sets the exception message
        :param value: the new error message
        """
        self.__message = value

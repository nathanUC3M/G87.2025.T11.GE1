from UC3MMoney1.TransactionRequest import TransactionRequest
from UC3MMoney1.TransactionManager import TransactionManager
from UC3MMoney1.TransactionManagementException import TransactionManagementException


print(TransactionManager.validate_iban("GB82WEST12345698765432"))  # true
print(TransactionManager.validate_iban("FR7630006000011234567890189")) #false
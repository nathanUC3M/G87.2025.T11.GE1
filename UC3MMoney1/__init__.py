from UC3MMoney1.TransactionRequest import TransactionRequest
from UC3MMoney1.TransactionManager import TransactionManager
from UC3MMoney1.TransactionManagementException import TransactionManagementException


print(TransactionManager.ValidateIBAN("GB82WEST12345698765432"))  # true
print(TransactionManager.ValidateIBAN("FR7630006000011234567890189")) #false
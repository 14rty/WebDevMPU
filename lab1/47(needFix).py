# Задание 4.7
'''
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида: 
„101010101010101010111011101110111100110011001100“

Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
'''
def z7():
    mac = "AAAA:BBBB:CCCC"
    mac = mac.replace("A", "1010")
    mac = mac.replace("B", "1011")
    mac = mac.replace("C", "1100")
    mac = mac.replace(":", "")
    print(mac)

z7()
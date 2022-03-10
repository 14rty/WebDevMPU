# Задание 4.2

'''
Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX 
Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.
'''
def z2():
    mac = "AAAA:BBBB:CCCC"
    mac = mac.replace(":", ".")
    print(mac)

z2()
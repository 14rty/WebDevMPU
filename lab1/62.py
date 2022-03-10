# 6.2
'''
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
«unicast» - если первый байт в диапазоне 1-223
«multicast» - если первый байт в диапазоне 224-239
«local broadcast» - если IP-адрес равен 255.255.255.255
«unassigned» - если IP-адрес равен 0.0.0.0
«unused» - во всех остальных случаях

'''

input = input('Введите адресс в формате "10.0.1.1":')
ip = input.split(".")

if (int(ip[0]) >= 1) & (int(ip[0]) <= 223):
    print("unicast")
elif (int(ip[0]) >= 224) & (int(ip[0]) <= 239):
    print("multicast")
elif (ip[0] == 255) & (ip[0] == ip[1]) & (ip[1] == ip[2]) & (ip[2] == ip[3]):
    print("local broadcast")
elif (ip[0] == 0) & (ip[0] == ip[1]) & (ip[1] == ip[2]) & (ip[2] == ip[3]):
    print("unassigned")
else:
    print("unused")
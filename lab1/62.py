# 6.2

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
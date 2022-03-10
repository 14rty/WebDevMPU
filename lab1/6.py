# 6.1

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for address in mac:
    result.append(address.replace(":", "."))
print(result)

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

# 6.2a

input = input('Введите адресс в формате "10.0.1.1":')
ip = input.split(".")

flag = True
i = 0
while flag == True:
    if ( int(ip[i]) >= 0 ) & ( int(ip[i]) <= 255 ) == False :
        flag = False
    i += 1
    
if flag == True:
    if (len(ip) == 4) & flag == True:
    
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
    else:
        print("Неверный ip-адрес")
else: 
    print("Неверный ip-адрес")

# 6.2b

glob_flag = False


while glob_flag == False:

    inp = input('Введите адресс в формате "10.0.1.1":')
    ip = inp.split(".")
    
    flag = True
    i = int(0)

    while (flag == True) & ( i <= 3 ):
        if ( ( int(ip[i]) >= 0 ) & ( int(ip[i]) <= 255 ) == False )  :
            flag = False
        i += 1
        
    if flag == True:
        if (len(ip) == 4) & flag == True:
            glob_flag = True
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
        else:
            print("Неверный ip-адрес")
    else: 
        print("Неверный ip-адрес")
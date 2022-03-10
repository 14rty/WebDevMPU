# Задание 4.1
def z1():
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    nat = nat.replace("Fast", "Gigabit")
    print(nat)

z1()
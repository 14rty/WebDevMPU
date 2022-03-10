# Задание 4.3
def z3():
    config = "switchport trunk allowed vlan 1,3,10,20,30,100"
    print(config.split()[4].split(","))

z3()
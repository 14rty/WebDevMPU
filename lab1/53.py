#5.3
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template = {'access': access_template, 'trunk':trunk_template }

mode = input("Введите режим работы интерфейса (access/trunk): ")

type_and_number = input("Введите тип и номер интерфейса: ")

vlans = input("Введите номер влан(ов): ")

print("interface {type_and_number}".format(type_and_number = type_and_number))
print("\n".join(template[mode]).format(vlans))

#5.3
'''
Скрипт должен запрашивать у пользователя:

информацию о режиме интерфейса (access/trunk)
номере интерфейса (тип и номер, вида Gi0/3)
номер VLANа (для режима trunk будет вводиться список VLANов)
В зависимости от выбранного режима, на стандартный поток вывода, 
должна возвращаться соответствующая конфигурация access или trunk 
(шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, 
а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

'''
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

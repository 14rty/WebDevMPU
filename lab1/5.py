#5.1
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

device = input("Введите имя устройства: ")
print(london_co[device])

#5.1a
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("Введите имя устройства: ")
parameter = input("Введите имя параметра: ")
print(london_co[device][parameter])

#5.1b
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("Введите имя устройства: ")
parameters = ",".join(london_co[device].keys())
parameter = input(f"Введите имя параметра ({parameters}): ")
print(london_co[device][parameter])

#5.1c
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("Введите имя устройства: ")
parameters = ",".join(london_co[device].keys())
parameter = input(f"Введите имя параметра ({parameters}): ")
print(london_co[device].get(parameter, "Такого параметра нет"))

#5.1d
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("Введите имя устройства: ")
parameters = ",".join(london_co[device].keys())
parameter = input(f"Введите имя параметра ({parameters}): ")
print(london_co[device].get(parameter.lower(), "Такого параметра нет"))

#5.2
net = input ("Введите IP-сеть в формате: 10.1.1.0/24: ")

ip, mask = net.split("/")
ip = ip.split(".")
mask = int(mask)
print(ip)
bin_mask = "1" * mask + "0" * (32-mask)
print(bin_mask)
ip_template = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""
oct1, oct2, oct3, oct4 = [int(bin_mask[0:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:32], 2)]

mask_template = """
Mask:
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_template.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
print(mask_template.format(mask, oct1, oct2, oct3, oct4))

#5.2a

network = input ("Введите IP-сеть в формате: 10.1.1.0/24: ")

ip, mask = network.split("/")
ip = ip.split(".")
mask = int(mask)

ip_bin = "{0:08b}{1:08b}{2:08b}{3:08b}".format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
print(ip_bin, "\n")

ip_network = ip_bin[:mask] + "0" * (32-mask)
print(ip_network, "\n")

bin_mask = "1" * mask + "0" * (32-mask)
print(bin_mask, "\n")

ip_template = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""
oct1, oct2, oct3, oct4 = [int(bin_mask[0:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:32], 2)]

mask_template = """
Mask:
/{0}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_template.format(int(ip_network[0:8], 2), int(ip_network[8:16], 2), int(ip_network[16:24], 2), int(ip_network[24:32], 2)))
print(mask_template.format(mask, oct1, oct2, oct3, oct4))

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

#5.3a
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

template = {'access': access_template, 
'trunk':trunk_template }

template_question = {'access': "Введите номер VLAN: ", 
'trunk':"Введите разрешенные VLANы: "}

mode = input("Введите режим работы интерфейса (access/trunk): ")
type_and_number = input("Введите тип и номер интерфейса: ")
vlans = input(template_question[mode])

print("interface {type_and_number}".format(type_and_number = type_and_number))
print("\n".join(template[mode]).format(vlans))
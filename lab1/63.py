# 6.3

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"], 
    "0/4": ["del", "17"]
}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

for intf, vlan in trunk.items():
    print("interface FastEthernet" + intf)
    for command in trunk_template:
        if command.endswith("allowed vlan"):
            buffer = ",".join(vlan[1:])

            if vlan[0] == "only":
                print(f" {command} {buffer}")
            elif vlan[0] == "del":
                print(f" {command} remove {buffer}")
            else:
                print(f" {command} {vlan[0]} {buffer}")
        else:
            print(f" {command}")
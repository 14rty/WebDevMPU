trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_trunk_config(trunk_mode_template, trunk_config):
    result = []
    for interface, vlan in trunk_config.items():
        result.append(f'Interface {interface}')
        for line in trunk_mode_template:
            if line.endswith("vlan"):
                line = line + "" + str(vlan).strip("[]")
            result.append(line)

    return result

result = generate_trunk_config(trunk_mode_template, trunk_config)
print(result)
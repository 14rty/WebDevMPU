# Задача 9.1
access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

def generate_access_config(intf_vlan_mapping, access_template):
    result = []
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    for interface, vlan in intf_vlan_mapping.items():
        for line in access_template:
            result.append(f'Interface {interface}')
            if line.endswish('vlan'):
                line = line + ' ' + str(vlan)
                result.append(line)
            else:
                result.append(line)
        return result

# Задача 9.1а

def generate_access_config_2(intf_vlan_mapping, access_template, psecurity = None):
    result = []
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    for interface, vlan in intf_vlan_mapping.items():
        for line in access_template:
            result.append(f'Interface {interface}')
            if line.endswith('vlan'):
                line = line + ' ' + str(vlan)
                result.append(line)
            else:
                result.append(line)
        if psecurity != None:
            result.extend(psecurity) 
        return result

result = generate_access_config_2(access_config, access_mode_template, port_security_template)
print(result)
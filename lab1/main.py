# Задание 4.1
def z1():
    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    nat = nat.replace("Fast", "Gigabit")
    print(nat)
# Задание 4.2
def z2():
    mac = "AAAA:BBBB:CCCC"
    mac = mac.replace(":", ".")
    print(mac)
# Задание 4.3
def z3():
    config = "switchport trunk allowed vlan 1,3,10,20,30,100"
    print(config.split()[4].split(","))
# Задание 4.4
def z4():
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    result = list(set(vlans))
    result.sort()
    print(result)
    
# Задание 4.5
def z5():
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"
    result = ( set(command1.split()[4].split(",")) & set(command2.split()[4].split(",")) )
    print(sorted(result))

# Задание 4.6
def z6():
    ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
    ip1 = ospf_route.split(",")[0].split()
    ip1.remove("via")
    ip2 = [ospf_route.split(",")[1]] + [ospf_route.split(",")[2]]
    print(ip1, ip2)
    print("Prefix", " ", ip1[0])
    print("AD/Metric", " ", str(ip1[1])[1:-1])
    print("Next-Hop", " ", ip1[2])
    print("Last update", " ", ip2[0])
    print("Outbound Interface", " ", ip2[1])
# Задание 4.7
def z7():
    mac = "AAAA:BBBB:CCCC"
    mac = mac.replace("A", "1010")
    mac = mac.replace("B", "1011")
    mac = mac.replace("C", "1100")
    mac = mac.replace(":", "")
    print(mac)
# Задание 4.8
def z8():
    ip = "192.168.3.1"
    sub = ip.split(".")
    result = '''
    {0:<10}  {1:<10}  {2:<10}  {3:<10}
    {0:<010b}  {1:<010b}  {2:<010b}  {3:<010b}
    '''.format(int(sub[0]), int(sub[1]), int(sub[2]), int(sub[3]))
    print(result)
z8()

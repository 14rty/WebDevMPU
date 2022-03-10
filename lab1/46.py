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

z6()
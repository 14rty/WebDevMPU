# 7.1
template = '''
Prefix                {:20}
AD/Metric             {:20}
Next-Hop              {:20}
Last update           {:20}
Outbound Interface    {:20}
'''

with open("ospf.txt", "r") as list:
    for line in list:
        buffer = line.replace(",", "").replace("via", "").replace(
            "[", "").replace("]", "").split()
        print(template.format(buffer[1], buffer[2], buffer[3], buffer[4], buffer[5]))
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
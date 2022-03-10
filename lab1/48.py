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
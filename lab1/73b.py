# 7.3b
'''
Сделать копию скрипта задания 7.3a.

Переделать скрипт:

Запросить у пользователя ввод номера VLAN.
Выводить информацию только по указанному VLAN.
Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

'''
sort_list = []
vlan = int(input("Введите VLAN: "))

with open("CAM_table.txt", "r") as list:

    for line in list:
        line = line.split()
        if line and line[0][0].isdigit():
            sort_list.append([int(line[0]), line[1], line[3]])
            
sort_list.sort()
for item in sort_list:
    if item[0] == vlan:
        print("{:<4}      {:14}      {:7}".format(item[0], item[1], item[2]))
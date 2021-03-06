# 7.3a
'''
Сделать копию скрипта задания 7.3.

Переделать скрипт: Отсортировать вывод по номеру VLAN В результате должен получиться такой вывод:

10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9
Обратите внимание на vlan 1000 - он должен выводиться последним. 
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

'''
sort_list = []

with open("CAM_table.txt", "r") as list:

    for line in list:
        line = line.split()
        if line and line[0][0].isdigit():
            sort_list.append([int(line[0]), line[1], line[3]])

sort_list.sort()
for item in sort_list:
    print("{:<4}      {:14}      {:7}".format(item[0], item[1], item[2]))
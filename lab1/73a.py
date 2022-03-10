# 7.3a
sort_list = []

with open("CAM_table.txt", "r") as list:

    for line in list:
        line = line.split()
        if line and line[0][0].isdigit():
            sort_list.append([int(line[0]), line[1], line[3]])

sort_list.sort()
for item in sort_list:
    print("{:<4}      {:14}      {:7}".format(item[0], item[1], item[2]))
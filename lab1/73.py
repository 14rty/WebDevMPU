# 7.3
with open("CAM_table.txt", "r") as list:
    for line in list:
        line = line.split()
        if line and line[0][0].isdigit():
            print("{:4}      {:14}      {:7}".format(line[0], line[1], line[3]))
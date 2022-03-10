# 7.2a
ignore = ["duplex", "alias", "configuration"]

with open("config_sw1.txt", "r") as list:

    for line in list:
        if line[0] == "!" or ignore[0] in line or ignore[1] in line or ignore[2] in line:
            continue
        else:
            print(line, end="")
# 7.2
with open("config_sw1.txt", "r") as list:
    for line in list:
        if line[0] == "!":
            continue
        else:
            print(line, end="")
# 7.2b
ignore = ["duplex", "alias", "configuration"]
with open("config_sw1.txt", "r") as inp, open("output.txt", "w") as output:
    for line in inp:
        if line[0] == "!" or ignore[0] in line or ignore[1] in line or ignore[2] in line:
            continue
        else:
            output.write(line)
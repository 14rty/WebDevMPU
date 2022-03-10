# 7.2b
'''
Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода, 
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:

имя исходного файла конфигурации
имя итогового файла конфигурации
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore и строки, 
которые начинаются на „!“.

'''
ignore = ["duplex", "alias", "configuration"]
with open("config_sw1.txt", "r") as inp, open("output.txt", "w") as output:
    for line in inp:
        if line[0] == "!" or ignore[0] in line or ignore[1] in line or ignore[2] in line:
            continue
        else:
            output.write(line)
# 7.2a
'''
Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, 
которые указаны в списке ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt. 
Имя файла передается как аргумент скрипту.

'''
ignore = ["duplex", "alias", "configuration"]

with open("config_sw1.txt", "r") as list:

    for line in list:
        if (line[0] == "!") or (ignore[0] in line) or (ignore[1] in line) or (ignore[2] in line):
            continue
        print(line, end="")
#5.3a
'''
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима, 
задавались разные вопросы в запросе о номере VLANа или списка VLANов:

для access: «Введите номер VLAN:»
для trunk: «Введите разрешенные VLANы:»

'''
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template = {'access': access_template, 
'trunk':trunk_template }

template_question = {'access': "Введите номер VLAN: ", 
'trunk':"Введите разрешенные VLANы: "}

mode = input("Введите режим работы интерфейса (access/trunk): ")

type_and_number = input("Введите тип и номер интерфейса: ")

vlans = input(template_question[mode])

print("interface {type_and_number}".format(type_and_number = type_and_number))
print("\n".join(template[mode]).format(vlans))
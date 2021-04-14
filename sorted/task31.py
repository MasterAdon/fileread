import os

f_p = os.getcwd()
f_t = os.listdir(f_p)

file_list = []

name = []
line_count = []
text = []
for dr in f_t:
    gt = os.path.splitext(dr)
    if gt[1] == '.txt':
        file_list.append(dr)

for file in file_list:
    n = file
    name.append(n)
    with open(file, encoding='utf-8') as c:
        g = len(c.read().strip().split('\n'))
        line_count.append(g)
    with open(file, encoding='utf-8') as c:
        t = c.read()
        text.append(t)

coun_dict = dict(zip(name, line_count))  # Создали словарь со значением кол-ва строк

text_dict = dict(zip(name, text))  # Создали словарь с текстом

# Ключи в словарях одинаковые и по условиям задачи нам известны

sor_dict = {}  # Сортировка словаря кол-ва строк в соответсвии с условиями задачи

sor_key = sorted(coun_dict, key=coun_dict.get)

for a in sor_key:
    sor_dict[a] = str(coun_dict[a])
# print(sor_dict)

with open('task', 'w', encoding='utf-8') as m:
    m.write('2.txt \n')
    m.write(f"{sor_dict['2.txt']} \n")
    m.write(text_dict['2.txt'])  # В тексте изначально присутсвует \n
    m.write('1.txt \n')
    m.write(f"{sor_dict['1.txt']} \n")
    m.write(f"{text_dict['1.txt']} \n")
    m.write('3.txt \n')
    m.write(f"{sor_dict['3.txt']} \n")
    m.write(text_dict['3.txt'])


with open('task', encoding='utf-8') as t:
    task3 = t.read()


# print(task3) # Вывод третьего задания


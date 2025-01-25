import json
import random

def rand_ver(ver):
    n_1, n_2 = random.randint(0, 9), random.randint(0, 9)
    while n_1 == n_2:
        n_2 = random.randint(0, 9)
    return ver.replace('*', str(n_1)), ver.replace('*', str(n_2))

ver = str(input("Введите версию продукта: "))
with open('file.json', 'r') as f:
    json_str = json.load(f)
print("Изначальные шаблоны: ",json_str)
ver_arr = []
for k in json_str.keys():
    ver_1, ver_2 = rand_ver(json_str[k])
    while (ver_1 in ver_arr) or (ver_2 in ver_arr):
        ver_1, ver_2 = rand_ver(json_str[k])
    ver_arr.append(ver_1), ver_arr.append(ver_2)
print("Сгенерированные номера: ",ver_arr)
print("Отсортированные номера: ",sorted(ver_arr))

min_arr = []
for i in sorted(ver_arr):
    if i < ver:
        min_arr.append(i)
if len(min_arr) == 0:
    print("Нет версий меньше введенной.")
else: print("Номера меньше введенной версии: ", min_arr)

# Написать скрипт, который переконвертирует строку в целочисленное
# Пример:
# ["12", "15", "16", "17"] до
# [12, 15, 16, 17] после
# Требование:
# Использовать list comprehension

list1 = ["12", "15", "16", "17"]
list2 = [int(x) for x in list1]
print(list2)
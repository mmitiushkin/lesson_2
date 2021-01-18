my_list = [11, 10, 7, 4, 4, 3, 1]
a = int(input("Введите число: "))

for i in range(len(my_list)):
    el = my_list[i]
    if a >= el:
        my_list.insert(i, a)
        break
print(my_list)

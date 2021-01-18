my_list = []

a = input("Введите что-нибудь: ")

while a != "stop":
    my_list.append(a)
    a = input("Введите что-нибудь: ")

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        i += 2
else:
    i = 0
    while i < len(my_list)-1:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2

print(my_list)

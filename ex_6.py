my_list = []

name = []
val = []
kol = []
ei = []

my_dict = {'название': None,
           'цена': None,
           'количество': None,
           'ед': None}

desc = {'название': None,
        'цена': None,
        'количество': None,
        'ед': None}

i = 1

c = input("Continue?(yes or no): ")
while c != 'no':
    a = []

    desc['название'] = input("Название: ")
    desc['цена'] = int(input("Цена: "))
    desc['количество'] = int(input("Количетво: "))
    desc['ед'] = input("Единица измерения: ")

    a.append(i)
    a.append(desc.copy())
    a = tuple(a)
    my_list.append(a)

    name.append(desc['название'])
    val.append(desc['цена'])
    kol.append(desc['количество'])
    ei.append(desc['ед'])

    my_dict['название'] = name
    my_dict['цена'] = val
    my_dict['количество'] = kol
    my_dict['ед'] = ei

    i += 1
    c = input("Continue?(yes or no): ")

print(my_list)
print(my_dict)
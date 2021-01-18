a = input('Введите слова: ')
count = 1

for i in a.split():
    print(f'{count} строка - {i[:10]}')
    count += 1

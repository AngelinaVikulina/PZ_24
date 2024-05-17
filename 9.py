# Вариант 5. Дан словарь с произвольным количеством элементов. Выяснить
# имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то
# добавить его в словарь. Вывести на экран измененный и первоначальный словарь.
fruits = {'овощ': 'морковь', 'ягода': 'клубника'}
print(f"Исходный словарь: {fruits} ")
if 'фрукт' in fruits and fruits['фрукт'] == 'яблоко':
    print('Элемент уже есть в словаре')
else:
    fruits['фрукт'] = 'яблоко'
    print('Элемент добавлен в словарь')
print(f"Измененный словарь: {fruits}")
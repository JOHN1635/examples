#!/usr/bin/python3

for i in range(2, 10):
	for j in range(2, 10):
		t = ' ' *(3 - len(str(i * j))) #  Корректируем размер отступа
		print(j, '*', i, '=', i * j, t, end='', sep='')
	print()

print('====================')
# Альтернативный вариант с рекурсией
def shiza(x, y):
	cell = str(x) + '*' + str(y) + '=' + str(x * y)
	border = ' ' * (3 - len(str(x * y)))
	if x < 9:
		return cell + border + str(shiza(x+1, y))
	return cell

for y in range(2, 10):
	print(shiza(2, y))

print('====================')
# Альтернативный вариант с двойной рекурсией
def shiza2(x, y):
	cell = str(x) + '*' + str(y) + '=' + str(x * y)
	border = ' ' * (3 - len(str(x * y)))
	if x < 9:
		return cell + border + str(shiza2(x + 1, y))
	elif y < 9:
		return cell + '\n' + str(shiza2(2, y + 1))
	return cell

print(shiza2(2, 2))

print('====================')
# Альтернативный вариант с генератором
[print(*[str(x) + '*' + str(y) + '=' + str(x * y) for y in range(2, 10)]) for x in range(2,10)]
# Можно воткнуть и формулу выравнивания отступа, но тогда строка вообще уползёт

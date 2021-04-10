#!/usr/bin/python3
def pyramid(size, s='*'):
	'''Печатаем пирамидку для Максика заданной высотой, символом s='''
	for i in range(size + 1):
		print(' ' * (size - i*2 // 2) + s + s * (i * 2))

for i in range(3, 33):
	pyramid(i)

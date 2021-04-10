#!/usr/bin/python3
from time import sleep
pose1 = '''
 (•_•)
 <) )╯
  / \ '''
pose2 = ''' 
\(•_•)
  ( (>
  / \ '''

for i in range(5):
	print(pose1)
	sleep(0.5)
	print(pose2)
	sleep(0.5)
	
def groupframe(a, b, n=1):
	a = a.split('\n')
	b = b.split('\n')
	for i in range(len(a)):
		print((a[i] + '   ' + b[i] + '   ') * n)

for i in range(10):
	groupframe(pose1, pose2, n=3)
	sleep(0.5)
	groupframe(pose2, pose1, n=3)
	sleep(0.5)

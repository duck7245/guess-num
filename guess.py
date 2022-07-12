import random
r = random.randint(1, 100)
count = 0
while True:
	count = count + 1	
	num = input('請猜數字(整數): ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	
	elif num > r:
		print('比答案大','已經猜了', count, '次了')
	
	elif num < r:
		print('比答案小','已經猜了', count, '次了')
	
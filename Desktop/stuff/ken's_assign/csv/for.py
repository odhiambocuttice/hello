

"""
numbers=[1,2,3,4,5]

for num in numbers:
	if num == 3:
		print('found')
		continue
	print(num)



n = 5
while n > 0:
	n -= 1
	print(n)
else:
	print('Loop done.')
"""

# guess code


"""fruits= ['mango','apple','grapes','guava','orange',]

for fruit in fruits:
	print(fruit)


print('tasty')"""


num = int(input('number:'))
factorial = 1

if num < 0:
    print('is positive')
elif num == 0:
    print('factorial =1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)

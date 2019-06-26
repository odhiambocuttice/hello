import random


# while True:
# 	print('meee')
# 	break

# i =1
# while i<= 5:
# 	  i+=1
# 	print(i)
# 	break



n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
	guess = int(input('new number:'))
	if guess > 0:
		if guess > to_be_guessed:
		    print("number too large")
		elif guess < to_be_guessed:
			print('number too small')
	else:
		print("sorry ")
	    
else:
	 print("congrats")	


    	         
 
      
travelling = input("yes or no:")
while travelling == 'yes':
	num = int(input("number of pple travelling"))


	for num in range(1, num+1):
		name = input('name:')
		age = input('age')
		sex = input('male or female')

		print(name)
		print(age)
		print(sex)

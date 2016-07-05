import random


Min=0
Max=500000
Done=False
NOG=0
while Done == False:
	Number=input("Number: ")
	try:
		Number=int(Number)
		Done=True
	except:
		print("Only numbers between %s and %s please."% (Min, Max))
Done=False
while Done==False:
	Guess=random.randint(Min,Max)
	NOG+=1
	if Guess == Number:
		print("Guess %s: %s" % (NOG, Guess))
		print("Win")
		Done=True
	elif Guess > Number:
		Max=Guess-1
		print("Guess %s: %s" % (NOG, Guess))
	else:
		Min=Guess+1
		print("Guess %s: %s" % (NOG, Guess))
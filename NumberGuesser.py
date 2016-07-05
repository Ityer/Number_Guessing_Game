import random
Number=int(input("Number: "))

Min=0
Max=500000
Done=False
NOG=0
while Done==False:
	Guess=random.randint(Min,Max)
	if Guess == Number:
		print("Win")
		Done=True
	elif Guess > Number:
		Max=Guess-1
		NOG+=1
		print("Guess %s: %s" % (NOG, Guess))
	else:
		Min=Guess+1
		NOG+=1
		print("Guess %s: %s" % (NOG, Guess))
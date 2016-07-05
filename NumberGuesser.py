import random


Min=0
Max=500000
Done=False
NOG=0
def humanGiver():
	Done=False
	while Done == False:
		Number=input("Number: ")
		try:
			Number=int(Number)
			Done=True
		except:
			print("Only numbers between %s and %s please."% (Min, Max))
	return Number

def robotGiver():
	Number = random.randint(Min,Max)
	return Number

while Done == False:
	RorH = input("(R)obot or (H)uman giver: ")
	if RorH == "R" or RorH == "r":
		Number=robotGiver()
		Done=True
	elif RorH == "H" or RorH == "h":
		Number=humanGiver()
		Done=True
	else:
		print("'R' or 'H'. Please don't put any other input")
Done=False
while Done==False:
	Guess=random.randint(Min,Max)
	NOG+=1
	if Guess == Number:
		print("Guess %s: %s" % (NOG, Guess))
		print("Won in %s guesses"% NOG)
		Done=True
	elif Guess > Number:
		Max=Guess-1
		print("Guess %s: %s" % (NOG, Guess))
	else:
		Min=Guess+1
		print("Guess %s: %s" % (NOG, Guess))
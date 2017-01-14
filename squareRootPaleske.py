#PSYCH420 - Square Root Exercise

#Equations for f(x)=x^2 and derivative:
#These functions take in your guess, and the value (val) that you 
#	want to find the cube root for.
def error(guess,val):
	return guess**2 - val

def derivEqu(guess):
	return 2*guess

#Newton's method equation to approximate a new guess:
def approx(guess,val):
	return guess - (error(guess,val)/float(derivEqu(guess)))

#Finding the cube of the val. Will continue to use your initial 
#	guess until the updated guess is within threshold value. If
#	there is no true cube root for the val, it is approximated. 
def findSquare(guess,val):
	threshold=0.0001
	if abs(approx(guess,val)**2 - val)<threshold:
		return round(approx(guess,val),3)
	else:
		updtGuess=approx(guess,val)
		return findSquare(updtGuess,val)

#Examples:
findCube(3,4)
2.0

findCube(4,47)
6.856

findCube(3,64)
8.0
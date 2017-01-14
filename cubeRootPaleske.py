#PSYCH420 - Cube Root Exercise

#Equations for f(x)=x^2 and derivative:
#These functions take in your guess, and the value (val) that you 
#	want to find the cube root for.
def error(guess,val):
	return guess**3 - val

def derivEqu(guess):
	return 3*guess**2

#Newton's method equation to approximate a new guess:
def approx(guess,val):
	return guess - (error(guess,val)/float(derivEqu(guess)))

#Finding the cube of the val. Will continue to use your initial 
#	guess until the updated guess is within threshold value. If
#	there is no true cube root for the val, it is approximated. 
def findCube(guess,val):
	threshold=0.0001
	if abs(approx(guess,val)**2 - val)<threshold:
		return round(approx(guess,val),3)
	else:
		updtGuess=approx(guess,val)
		return findCube(updtGuess,val)

#Examples:
>>> findCube(7,125)
5.0
>>> findCube(6,216)
6.0
>>> findCube(5.5,216)
6.0
>>> findCube(2,64)
4.0
>>> findCube(2,65)
4.021 
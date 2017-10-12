import pyautogui, random, time

# Images
ZERO = "Images/0.png"
ONE = "Images/1.png"
TWO = "Images/2.png"
THREE = "Images/3.png"
FOUR = "Images/4.png"
FIVE = "Images/5.png"
SIX = "Images/6.png"
SEVEN = "Images/7.png"
EIGHT = "Images/8.png"
NINE = "Images/9.png"
DIVIDE = "Images/divide.png"
EQUALS = "Images/equals.png"
MINUS = "Images/minus.png"
PLUS = "Images/plus.png"
TIMES = "Images/times.png"


def within(area):
	# Returns a random pixel within a given area

	minX = area[0]
	minY = area[1]
	maxX = area[0] + area[2]
	maxY = area[1] + area[3]

	randomSpot = (random.randint(minX, maxX), random.randint(minY, maxY))
	return randomSpot

def moveToButton(button):
	# Function will move the cursor to the given button (image) if the calculator is on the screen

	loc = pyautogui.locateOnScreen(button)
	if loc != None:
		spot = within(loc)
		pyautogui.moveTo(spot, duration = 0.25)
		pyautogui.click()
		time.sleep(1)
	else:
		raise Exception("Cannot find the calculator.")

def userInput():
	command = input("Please enter your command: ")
	return command

def doThings(userInput):
	if type(userInput) == str:
		for character in userInput:
			if character == "0":
				moveToButton(ZERO)
			elif character == "1":
				moveToButton(ONE)
			elif character == "2":
				moveToButton(TWO)
			elif character == "3":
				moveToButton(THREE)
			elif character == "4":
				moveToButton(FOUR)
			elif character == "5":
				moveToButton(FIVE)
			elif character == "6":
				moveToButton(SIX)
			elif character == "7":
				moveToButton(SEVEN)
			elif character == "8":
				moveToButton(EIGHT)
			elif character == "9":
				moveToButton(NINE)
			elif character == "/":
				moveToButton(DIVIDE)
			elif character == "*":
				moveToButton(TIMES)
			elif character == "+":
				moveToButton(PLUS)
			elif character == "-":
				moveToButton(MINUS)
		moveToButton(EQUALS)

	else:
		raise Exception("That's not a string. ")

def main():
	# Main program function
	commandString = userInput()
	doThings(commandString)

# Call main function
if __name__ == '__main__':
	main()
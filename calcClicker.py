import pyautogui, random, time

# Images
ZERO = "0.png"
ONE = "1.png"
TWO = "2.png"
THREE = "3.png"
FOUR = "4.png"
FIVE = "5.png"
SIX = "6.png"
SEVEN = "7.png"
EIGHT = "8.png"
NINE = "9.png"
DIVIDE = "divide.png"
EQUALS = "equals.png"
MINUS = "minus.png"
PLUS = "plus.png"
TIMES = "times.png"


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
	else:
		raise Exception("Cannot find the calculator.")


def main():
	# Main program function

	# For right now, this area is for debugging purposes
	# For example, right now the program will move to 5, wait 2 seconds, then move to 4.

	moveToButton(FIVE)
	time.sleep(2)
	moveToButton(FOUR)

# Call main function
if __name__ == '__main__':
	main()
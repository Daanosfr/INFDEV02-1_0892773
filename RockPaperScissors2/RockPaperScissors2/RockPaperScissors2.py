import random;
player = raw_input("Enter your choice (rock/paper/scissors/spock/lizard): ")
player = player.lower()

while (player != "rock" and player != "paper" and player != "scissors"  and player != "spock"  and player != "lizard" ):
	print(player)
	player = raw_input("That choice is not valid. Enter your choice (rock/paper/scissors/spock/lizard): ")
	player = player.lower()

computerInt = random.randint(0,4)
if (computerInt == 0):
	computer = "rock"
elif (computerInt == 1):
	computer = "paper"
elif (computerInt == 2):
	computer = "scissors"
elif (computerInt == 3):
	computer = "lizard"
elif (computerInt == 4):
	computer = "spock"

print "The computer choose: ", computer
if (player == computer):
	print("Draw!");
elif (player == "rock"):
	if (computer == "paper" or computer == "spock"):
		print "Computer wins!"
	elif (computer == "lizard" or computer == "scissors"):
		print "You win!"
elif (player == "paper"):
	if (computer == "scissors" or computer == "lizard"):
		print "Computer wins!" 
	elif (computer == "spock" or computer == "rock"):
		print "You win!" 
elif (player == "scissors"):
	if (computer == "rock" or computer == "spock"):
		print "Computer wins!"
	elif (computer == "lizard" or computer == "scissors"):
		print "You win!"
elif (player == "spock"):
	if (computer == "paper" or computer == "lizard"):
		print "Computer wins!"
	elif (computer == "rock" or computer == "scissors"):
		print "You win!"
elif (player == "lizard"):
	if (computer == "scissors" or computer == "rock"):
		print "Computer wins!"
	elif (computer == "paper" or computer == "spock"):
		print "You win!"
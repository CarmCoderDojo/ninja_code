import random

player1_dice = []
player2_dice = []
player3_dice = []

for i in range(2):
	player1_dice.append(random.randint(1,3))
	player2_dice.append(random.randint(1,3))
	player3_dice.append(random.randint(1,3))

print("Player 1 rolled" + str(player1_dice))
print("Player 2 rolled" + str(player2_dice))
print("Player 3 rolled" + str(player3_dice))

if sum(player1_dice) > sum(player2_dice) and sum(player1_dice) > sum(player3_dice):
	print("Player 1 Wins")
elif sum(player2_dice) > sum(player1_dice) and sum(player2_dice) > sum(player3_dice):
	print("Player 2 Wins")
elif sum(player3_dice) > sum(player1_dice) and sum(player3_dice) > sum(player2_dice):
	print("Player 3 Wins")
elif sum(player1_dice) == sum(player2_dice) and sum(player2_dice) == sum(player3_dice):
	print("Players 1/2/3, Draw")
elif sum(player1_dice) == sum(player2_dice):
	print("Players 1/2, Draw")
elif sum(player1_dice) == sum(player3_dice):
	print("Players 1/3, Draw")
elif sum(player2_dice) == sum(player3_dice):
	print("Players 2/3, Draw")

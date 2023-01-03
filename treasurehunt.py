#treasure hunt
print('Welcome to treasure island\nYour misson is to find the treasure')

left_right = input("You're at a cross road.Where do you want to go ? type left or right\n")
if left_right=='left':
    wait_swim = input("You come to lake.There is an island in the middle of the lake. Type 'wait' to wait for a boat.Type 'swim' to swim across\n")
    if wait_swim=='wait':
        doors = input("You arrived at island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which color do you choose?\n")
        if doors=='yellow':
            print('you win!!!!')
        else:
            print('game over!,the dragon in room attcked you')
    else:
        print('Game over!,shark ate you')
else:
    print('game over!, you fell into a hole')







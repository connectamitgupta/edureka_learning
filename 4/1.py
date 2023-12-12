'''A Robot moves in a Plane starting from the origin point (0,0). The robot can move
toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given
following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps. Write a program to compute the
distance current position after sequence of movements.
Hint: Use math module.
'''

# Python3 implementation to find final position
# of robot after the complete movement
 
# function to find final position of
# robot after the complete movement
 
 
def finalPosition(move):
 
    l = len(move)
    countUp, countDown = 0, 0
    countLeft, countRight = 0, 0
 
    # traverse the instruction string
    # 'move'
    for i in range(l):
 
        # for each movement increment
        # its respective counter
        if (move[i] == 'U'):
            countUp += 1
 
        elif(move[i] == 'D'):
            countDown += 1
 
        elif(move[i] == 'L'):
            countLeft += 1
 
        elif(move[i] == 'R'):
            countRight += 1
 
    # required final position of robot
    print("Final Position: (", (countRight - countLeft),
          ", ", (countUp - countDown), ")")
 
 
# Driver code
if __name__ == '__main__':
    # move = "UDDLLRUUUDUURUDDUULLDRRRR"
    move = "UUUUUDDDLLLRR"
  
    finalPosition(move)
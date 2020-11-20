import numpy as np
from time import perf_counter

FAILED = False

# heuristic fuction
# manhattan_distance
def ManhattanDistance(board,t):
    distance = 0
    for i in range(len(board)):
        distance += abs(i/t - board[i]/t) + abs(i%t - board[i]%t)
    return distance

# function which defines next possible move:
def move_HillClimbing(board,t):
    for i in range(len(board)):
        if board[i] == 0:      #i contains position of blank space
            break
    distanceBoard = {}
    if i >= 3:
        up = list(board)
        up[i] = board[i-3]
        up[i-3] = 0
        distanceBoard[i-3] = ManhattanDistance(up,t)
    if i < 6:
        down = list(board)
        down[i] = board[i+3]
        down[i+3] = 0
        distanceBoard[i+3] = ManhattanDistance(down,t)
    if i%3 != 0:
        left = list(board)
        left[i] = board[i-1]
        left[i-1] = 0
        distanceBoard[i-1] = ManhattanDistance(left,t)
    if (i+1)%3 != 0:
        right = list(board)
        right[i] = board[i+1]
        right[i+1] = 0
        distanceBoard[i+1] = ManhattanDistance(right,t)
    
    shortestDistance = ManhattanDistance(board,t)
    for point,value in distanceBoard.items():
        # "<=" means "not worse than" situation
        # plain
        if value <= shortestDistance:
            shortestDistance = value
    
    shortestDistancePoints = []
    for point,value in distanceBoard.items():
        if value == shortestDistance:
            shortestDistancePoints.append(point)
    
    # can not find a steeper move
    # we have come to the peek(local optimization)
    if len(shortestDistancePoints) == 0:
        global FAILED
        FAILED = True
        return board
    
    np.random.shuffle(shortestDistancePoints)
    board[i] = board[shortestDistancePoints[0]]
    board[shortestDistancePoints[0]]= 0
    return board

def solution_HillClimbing(board,t):
    maxRound = 2000
    count = 0
    while True:
        collision = ManhattanDistance(board,t)
        if collision == 0:  #present state same as goal state 
            return board
        board = move_HillClimbing(board,t)
        count += 1
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
    
def main():
    title = "N-PuzzleHillClimbing"
    n=int(input("enter value of n "))
    print(str(n)+"-PuzzleHillClimbing")    
    
    t=int((n+1)**0.5)  #no. of elements in a row
    startTime = perf_counter()
    successCase = 0
    totalCase = 0
    result = title + " result:\n\n"
    with open("TestBoard.txt", "r") as ins:
        for line in ins:
            global FAILED
            FAILED = False
            totalCase += 1
            board = []
            for col in line.split():
                board.append(int(col))
            board = solution_HillClimbing(board,t)
            if FAILED:
                result += "Failed!"
                print("case:",totalCase," ->Failed!")
            else:
                print("case:",totalCase," ->Success")
                successCase += 1
                result+="Success"
            result += "\n"
            if totalCase>=10:
                break
    
    endTime = perf_counter()
    result += "\nTotal time: " + str(endTime - startTime) + '\n'
    time=str(endTime - startTime)
    print("Total time:"+time)
    result += "Total case number: " + str(totalCase) + ", Success case number: " + str(successCase) + '\n'
    totalcase=str(totalCase)
    print("Total case number: "+ totalcase)
    successcase=str(successCase)
    print("Success case number: "+successcase)
    result += "Success rate: " + str(successCase / float(totalCase)) + '\n'
    successrate=str(successCase / float(totalCase))
    print("Success rate: " +successrate)
    
    f = open(title + '.txt', 'w')
    f.write(result)
    f.close()
        
if __name__ == '__main__':
    main()


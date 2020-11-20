import numpy as np
import math
from time import perf_counter


FAILED = False

# heuristic cost
# manhattan_distance
def ManhattanDistance(board,t):
    distance = 0
    for i in range(len(board)):
        distance += abs(i/t - board[i]/t) + abs(i%t - board[i]%t)
    return distance

# function which defines next possible move:
def move_SimulatedAnnealing(board,t):
    temperature=len(board)
    AnnealingRate=0.95
    for i in range(len(board)):
        if board[i] == 0:  #i contains position of blank space
            break
    distance = ManhattanDistance(board,t)
    temperature=max(temperature*AnnealingRate,0.02)
    while True:
        randCase = np.random.randint(0,4)
        if randCase == 0:
            if i >= t:
                up = list(board)
                up[i] = board[i-t]
                up[i-t] = 0
                if ManhattanDistance(up,t) < distance:
                    return up
                else:
                    deltaE=ManhattanDistance(up,t)-distance
                    AcceptProbability=min(math.exp(deltaE/temperature),1)
                    if np.random.random()<=AcceptProbability:
                        return up
        elif randCase == 1:
            if i < t*(t-1):
                down = list(board)
                down[i] = board[i+t]
                down[i+t] = 0
                if ManhattanDistance(down,t) < distance:
                    return down
                else:
                    deltaE=ManhattanDistance(down,t)-distance
                    AcceptProbability=min(math.exp(deltaE/temperature),1)
                    if np.random.random()<=AcceptProbability:
                        return down
        elif randCase == 2:
            if i%t != 0:
                left = list(board)
                left[i] = board[i-1]
                left[i-1] = 0
                if ManhattanDistance(left,t) < distance:
                    return left
                else:
                    deltaE=ManhattanDistance(left,t)-distance
                    AcceptProbability=min(math.exp(deltaE/temperature),1)
                    if np.random.random()<=AcceptProbability:
                        return left                
        else:    
            if (i+1)%t != 0:
                right = list(board)
                right[i] = board[i+1]
                right[i+1] = 0
                if ManhattanDistance(right,t) < distance:
                    return right
                else:
                    deltaE=ManhattanDistance(right,t)-distance
                    AcceptProbability=min(math.exp(deltaE/temperature),1)
                    if np.random.random()<=AcceptProbability:
                        return right        
    return board

def solution_SimulatedAnnealing(board,t):
    maxRound = 250000
    count = 0
    while True:
        collisionNum = ManhattanDistance(board,t)
        if collisionNum == 0:
            return board
        board = move_SimulatedAnnealing(board,t)
        count += 1
        if(count >= maxRound):
            global FAILED
            FAILED = True
            return board
    
def main():
    title = "N-PuzzleSimulatedAnnealingHillClimbing"
    n=input("enter value of n ")
    print(str(n)+"-PuzzleSimulatedAnnealingHillClimbing")
    n=int(n)
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
            board = solution_SimulatedAnnealing(board,t)
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


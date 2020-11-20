import numpy as np

def step(board,t):
    for i in range(len(board)):
        if board[i] == 0:
            break

    while True:
        randCase = np.random.randint(0,4)
        if randCase == 0:
            if i >= t:
                up = list(board)
                up[i] = board[i-t]
                up[i-t] = 0
                return up
        elif randCase == 1:
            if i < t*(t-1):
                down = list(board)
                down[i] = board[i+t]
                down[i+t] = 0
                return down
        elif randCase == 2:
            if i%t != 0:
                left = list(board)
                left[i] = board[i-1]
                left[i-1] = 0
                return left
        else:    
            if (i+1)%t != 0:
                right = list(board)
                right[i] = board[i+1]
                right[i+1] = 0
                return right
        
    return board

def generate(board,t):
    maxStep = 5000
    count = 0
    while True:
        board = step(board,t)
        count += 1
        if(count >= maxStep):
            return board
    

def main():
    n=int(input("Enter value of n "))
    t=int((n+1)**0.5) #no. of elements in a row
    f = open("TestBoard.txt", "w")
    testCaseCount =int(input("Enter no. of Test cases "))
    result = ""
    while testCaseCount > 0:
        board = [i for i in range(n+1)]
        testCaseCount -= 1
        
        board = generate(board,t)
        
        for i in range(0,n): 
            result += str(board[i]) + ' '
        result += str(board[i+1]) + '\n' 
    f.write(result)
    f.close()
    print("Test cases have been generated!")
    
if __name__ == '__main__':
    main()
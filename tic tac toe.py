def sum(a,b,c):
    return a+b+c 

def print_borad(xstate,zstate):
    zero="X" if xstate[0] else ("O" if zstate[0] else 0)
    one="X" if xstate[1] else ("O" if zstate[1] else 1)
    two="X" if xstate[2] else ("O" if zstate[2] else 2)
    three="X" if xstate[3] else ("O" if zstate[3] else 3)
    four="X" if xstate[4] else ("O" if zstate[4] else 4)
    five="X" if xstate[5] else ("O" if zstate[5] else 5)
    six="X" if xstate[6] else ("O" if zstate[6] else 6)
    seven="X" if xstate[7] else ("O" if zstate[7] else 7)
    eight="X" if xstate[8] else ("O" if zstate[8] else 8) 

    print(f"{zero} | {one} | {two} ")
    print("--|-- |--")
    print(f"{three} | {four} | {five} ")
    print("--|-- |--")
    print(f"{six} | {seven} | {eight} ")

    
def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1        

print("welcome to tic tac toe")
xstate= [0,0,0,0,0,0,0,0,0]
zstate= [0,0,0,0,0,0,0,0,0]
turn = 1 # 1 for X and 0 for O
while (True):    
    print_borad(xstate,zstate)
    if (turn == 1):
        print("X's chance")
        value = int(input("please enter a value: "))
        xstate[value] = 1
    else:
        print("o's chance")
        value = int(input("please enter a value: "))
        zstate[value] = 1
    
    turn = 1 - turn
    cwin =  checkWin(xstate,zstate)
    
    if (cwin != -1):
        print("match over!")
        break
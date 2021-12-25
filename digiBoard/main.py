
from pyBoard import *
move_list=[]

def isValidInput(list):
    row   = list[0]
    array = list[1] 

    c1 = len(list) == 2
    c2 = row in [1,2,3,4,5,6,7,8] # range(1,9)
    c3 = True 

    for i in array:
        if i != 1 or 0:
            c3= False
    


def getMove(row,list): 
    
    Final_move=''
    # befor sending insure that the list is valid
    # list = [<row number>,[<postion list>]]  ie. list = [3,[0,1,0,0,0,0,0,0]]

   
    move = getNotation(row,list)
    move_list.append(move)
    #print(move_list)


    if isNormalMove(move_list)==True:
        Final_move = makeNormalMove(move_list)
        move_list.clear()
 
    elif isCaptureMove(move_list):
        Final_move = makeCaptureMove(move_list)
        move_list.clear()

    return Final_move



print(getMove(1,[1,1,1,1,1,1,1,0]))
print(getMove(1,[1,1,1,1,1,1,0,0]))
print(getMove(1,[1,1,1,1,1,1,0,1]))

print(getMove(1,[1,1,1,1,1,0,0,1]))
print(getMove(1,[1,1,1,1,1,0,1,1]))

print(getMove(1,[1,1,1,1,1,0,0,1]))
print(getMove(1,[1,1,1,1,1,0,0,0]))
print(getMove(1,[1,1,1,1,1,0,0,1]))

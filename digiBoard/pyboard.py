import numpy as np


old_matrix = np.array([[ 1, 1, 1, 1 ], 
                       [ 0, 0, 0, 0 ], 
                       [ 0, 0, 0, 0 ],  
                       [ 1, 1, 1, 1 ]])

new_matrix = np.array([[ 1, 1, 1, 1 ], # 4
                       [ 0, 0, 0, 0 ], # 3
                       [ 0, 0, 0, 0 ], # 2
                       [ 1, 1, 1, 1 ]])# 1
                    #    a  b  c  d


sign=[]
move=[]


def get_sign(matrix):
    #This function return True if matrix contain 1.  (place)
    #and False if it contain -1.   (pick)
    for i in  matrix:

        if np.sum(i)==1:
            return True

        elif np.sum(i)==-1:
            return False
            
def matrix_to_notation(matrix):
    '''
    this function return chess notation based of position on 1 or -1 in a 2D array
    '''
    #column is for alphabet
    #row is for number
    
    '''

    8 [1,1,1,1,1,1,1,1],
    7 [1,1,1,1,1,1,1,1],
    6 [0,0,0,0,0,0,0,0],
    5 [0,0,0,0,0,0,0,0],
    4 [0,0,0,0,0,0,0,0],
    3 [0,0,0,0,0,0,0,0],
    2 [1,1,1,1,1,1,1,1],
    1 [1,1,1,1,1,1,1,1]
       a b c d e f g h 

    '''
    a=np.where(matrix !=0) # IF NUMBER IS 1 OR -1
    
    rows=a[0]    # find the row where 1 or -1 is present
    column=a[1]  # find the column where 1 or -1 is present
       
    r,c=matrix.shape
    num= c-rows

    alp=chr(97+column[0])   # convert number to alphabet ie. 1->a , 2->b , 3->c and so on      
    notation=alp+str(num[0])  # alphabet and number

    #print(notation)
    return notation

def is_sufficent_move(a):
    # Check wether there is enough move or not
    # This function is called when the first element in list (list name -> "sign") is 
    # False (Pick) and last element is True (Place)
    if a[0]==False and a[-1]==True:
        return True
    else:
        return False

def update_new_matrix():
    # little bit of twiking in needed tho it work as intended

    '''
    this function take input a single row 
    ie."1001" first number represent row number 
    "001" represent valur of that row in matrix  
    new_matrit[1]=[0,0,1]
    '''
    a= input("Enter matrix")
    a.split()
    
    a= list(map(int, a))
    rows,columns=new_matrix.shape
    list_index=rows - a[0]
    new_matrix[list_index]=a[1:]
    #print(list_index)


##################################################################
################### DIFFERENT TYPE OF MOVES ######################
##################################################################

#.....................Normal move.................................
def normal_move():
    from_=move[0]
    to=move[1]
    sign.clear()
    move.clear()

    return from_+to
#.................................................................


#.....................Capture move................................
def capture_move(): 
    #refer notes to understand this
    if move[1]==move[2]:
        from_=move[1]
        to=move[0]
    elif move[1]!= move[2]:
        from_= move[1]
        to= move[0]
    move.clear()
    sign.clear()

    return from_ + to
#.................................................................


#.....................Castling....................................
def castling():
    pass
#.................................................................


#.................... En Passant Capture..........................
def En_Passant_Capture():
    pass
#.................................................................

#.....................Pawn Promotion..............................
def Pawn_Promotion():
    pass
#.................................................................

##################################################################
##################################################################
##################################################################



def main():
    while True:

        old_matrix=np.copy(new_matrix)
        update_new_matrix()

        #print(new_matrix)
        #print(old_matrix)

        resultant_matrix=new_matrix-old_matrix


        #....................................................
        Sign=get_sign(resultant_matrix)
        sign.append(Sign)
        Move=matrix_to_notation(resultant_matrix)
        move.append(Move)
        #....................................................


        #....................................................
        #print(f"Enough move is :{is_sufficent_move(sign)}")
        print(f'notation :{move}')
        print(f'Sign :{sign}')
        #....................................................
        
        if is_sufficent_move(sign)==True:

            if len(move)==2:
                print(normal_move())

            elif len(move)==3:
                print(capture_move()) 
        
if __name__=="__main__":
    main() # for testing purpose only

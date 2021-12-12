import numpy as np

old_matrix = np.array([[ 1, 1, 1, 1, 1, 1, 1, 1], 
                       [ 1, 1, 1, 1, 1, 1, 1, 1], 
                       [ 0, 0, 0, 0, 0, 0, 0, 0], 
                       [ 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 1, 1, 1, 1, 1, 1, 1, 1],
                       [ 1, 1, 1, 1, 1, 1, 1, 1]])

new_matrix = np.array([[ 1, 1, 1, 1, 1, 1, 1, 1], 
                       [ 1, 1, 1, 1, 1, 1, 1, 1], 
                       [ 0, 0, 0, 0, 0, 0, 0, 0], 
                       [ 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0],
                       [ 1, 1, 1, 1, 1, 1, 1, 1],
                       [ 1, 1, 1, 1, 1, 1, 1, 1]])
                        #a  b  c  d  e  f  g  h 

move=[]
sign=[]


#.........................................................................................          
def unit_matrix_to_notation(matrix):
    '''
    this function return chess notation based of position on 1 or -1 in a 2D array
    '''
    def get_sign(matrix_):
        #This function return True if matrix contain 1.  (place)
        #and False if it contain -1.   (pick)
        for i in  matrix_:

            if np.sum(i)==1:
                return "place"

            elif np.sum(i)==-1:
                return "pick"

    a=np.where(matrix !=0) # find array where 1 OR -1 is present.
    # a=[row,column] this is position of 1 OR -1
    rows=a[0]    # find the row where 1 or -1 is present
    column=a[1]  # find the column where 1 or -1 is present
       
    r,c=matrix.shape
    num= c-rows

    alp=chr(97+column[0])   # convert number to alphabet ie. 1->a , 2->b , 3->c and so on      
    notation=alp+str(num[0])  # alphabet and number
    #print(notation)

    sign_=get_sign(matrix)

    return [notation,sign_] # output formate [['d5', 'place']]

#.........................................................................................

def is_sufficent_move(a):
    # Check wether there is enough move or not
    # This function is called when the first element in list (list name -> "sign") is 
    # False (Pick) and last element is True (Place)
    if a[0]==False and a[-1]==True:
        return True
    else:
        return False

# make classes for moves

#.....................Normal move.................................
def normal_move():
    from_=move[0]
    to=move[1]
    
    move.clear()
    sign.clear()

    return from_+to
#.................................................................
   

#.....................Capture move................................
def capture_move(): 

    #refer notes to understand this
    # this function work as intended but it is complete mess
    if move[1]==move[2]:
        from_=move[1]
        to=move[0]
    elif move[1]!= move[2]:
        from_= move[1]
        to= move[0]
    move.clear()
    sign.clear()
  
    return  to + from_ # this 
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

def update_matrix(row_num,new_list):

    old_matrix = np.copy(new_matrix)  # Copy old matrix

    new_matrix[row_num]=new_list      # UPDATE THE NEW MATRIX WITH NEW ARRAY
   
    resultant_matrix=new_matrix-old_matrix  # Substract old matrix from new matrix 
 
    ab=unit_matrix_to_notation(resultant_matrix)   # find position of 1 or -1 and its sign
    # ab=[<notation>,<sign>]  
    
    move.append(ab[0])
    sign.append(ab[1])
#........................Determining move type.............................

    if len(move)==2 and (move[0]!= move[1]) and sign[0]=="pick" and  sign[1]=="place":
        return ["Normal move ",normal_move()]

    elif len(move)==3 and (move[2]==move[1] or move[2]==move[0]) :
        return ["Capture move ",capture_move()]



if __name__=="__main__": # for module testing ouly


    v=update_matrix(1,[0,1,1,1,1,1,1,1])
    v=update_matrix(1,[0,0,1,1,1,1,1,1])
    v=update_matrix(1,[0,1,1,1,1,1,1,1])
    print(v)
    v=update_matrix(1,[0,0,1,1,1,1,1,1])
    v=update_matrix(1,[1,0,1,1,1,1,1,1])
    print(sign)
    print(v)
    print(move)

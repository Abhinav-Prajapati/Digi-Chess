from tkinter import *
root = Tk()
root.title('ChessBoard sim')
import chess
import chess.engine
import pyboard as pb
import numpy as np



engine = chess.engine.SimpleEngine.popen_uci(r"D:\Projects\Digi-Chess\digiBoard\stockfish\stockfish_14.1_win_x64_avx2.exe")

board = chess.Board()

def ai(m):
    if m!= None:

        Nf3 = chess.Move.from_uci(m[1])
        board.push(Nf3)
        print(f'Your move {m[1]} \n')   
        print(board)
        print()
        result = engine.play(board, chess.engine.Limit(time=0.1))

        board.push(result.move)
        print(f'Computer move {result.move} \n' )
        print(board)
        print()





############################



var_matrix=[]

for i in range(8):

    a=[]
    for j in range(8):
        if i in [0,1,6,7]:
            a.append(IntVar(value=1)) # set last row to checked
        else:
            a.append(IntVar())

    var_matrix.append(a)


#print(var_matrix[0][0])
############################

ac=[]

def Update_row_1():

    a=[]
    for i in range(8):
        var=var_matrix[0][i]
        a.append(var.get())

    ac=pb.update_matrix(0,a)
    ai(ac)
def Update_row_2():
     
    a=[]
    for i in range(8):
        var=var_matrix[1][i]
        a.append(var.get())
    #print(2,a)
    ac=pb.update_matrix(1,a)
    ai(ac)

def Update_row_3():
    
    a=[]
    for i in range(8):
        var=var_matrix[2][i]
        a.append(var.get())
    #print(3,a)
    ac=pb.update_matrix(2,a)
    ai(ac)
def Update_row_4():
  
    a=[]
    for i in range(8):
        var=var_matrix[3][i]
        a.append(var.get())
    #print(4,a)
    ac=pb.update_matrix(3,a)
    ai(ac)
def Update_row_5():
     
    a=[]
    for i in range(8):
        var=var_matrix[4][i]
        a.append(var.get())
    #print(5,a)
    ac=pb.update_matrix(4,a)
    ai(ac)
def Update_row_6():
     
    a=[]
    for i in range(8):
        var=var_matrix[5][i]
        a.append(var.get())
    #print(6,a)
    ac=pb.update_matrix(5,a)
    ai(ac)
def Update_row_7():
     
    a=[]
    for i in range(8):
        var=var_matrix[6][i]
        a.append(var.get())
    ac=pb.update_matrix(6,a)
    ai(ac)
def Update_row_8():
     
    a=[]
    for i in range(8):
        var=var_matrix[7][i]
        a.append(var.get())
     
    ac= pb.update_matrix(7,a)
    ai(ac)

for i in range(8):  # row 1
    row_=0
    a=Checkbutton(root, text=chr(97+i)+'8',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_1)
    a.grid(row=row_,column=i)

for i in range(8):  # row 2
    row_=1
    b=Checkbutton(root, text=chr(97+i)+'7',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_2)
    b.grid(row=row_,column=i)

for i in range(8):  # row 3
    row_=2
    b=Checkbutton(root, text=chr(97+i)+'6',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_3)
    b.grid(row=row_,column=i)

for i in range(8):  # row 4
    row_=3
    b=Checkbutton(root, text=chr(97+i)+'5',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_4)
    b.grid(row=row_,column=i)

for i in range(8):  # row 5
    row_=4
    b=Checkbutton(root, text=chr(97+i)+'4',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_5)
    b.grid(row=row_,column=i)

for i in range(8):  # row 6
    row_=5
    b=Checkbutton(root, text=chr(97+i)+'3',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_6)
    b.grid(row=row_,column=i)

for i in range(8):  # row 7
    row_=6
    b=Checkbutton(root, text=chr(97+i)+'2',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_7)
    b.grid(row=row_,column=i)

for i in range(8):  # row 8
    row_=7
    b=Checkbutton(root, text=chr(97+i)+'1',variable=var_matrix[row_][i], onvalue=1, offvalue=0, command=Update_row_8)
    b.grid(row=row_,column=i)




root.mainloop()
    


    

import pyboard as pb
import numpy as np

def main():
    while True:

        old_matrix=np.copy(pb.new_matrix)
        pb.update_new_matrix()

        #print(new_matrix)
        #print(old_matrix)

        resultant_matrix=pb.new_matrix-old_matrix


        #....................................................
        Sign=pb.get_sign(resultant_matrix)
        pb.sign.append(Sign)
        Move=pb.matrix_to_notation(resultant_matrix)
        pb.move.append(Move)
        #....................................................


        #....................................................
        #print(f"Enough move is :{is_sufficent_move(sign)}")
        print(f'notation :{pb.move}')
        print(f'Sign :{pb.sign}')
        #....................................................
        
        if pb.is_sufficent_move(pb.sign)==True:

            if len(pb.move)==2:
                print(pb.normal_move())

            elif len(pb.move)==3:
                print(pb.capture_move()) 
        
main()
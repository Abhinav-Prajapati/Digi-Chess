import numpy as np


new_matrix = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
)


def unit_matrix_to_notation(matrix):
    # print(matrix,'result')
    """this function return chess notation based of position on 1 or -1 in a 2D array"""

    def get_sign(matrix_):
        # This function return True if matrix contain 1.  (place)
        # and False if it contain -1.   (pick)
        for i in matrix_:
            if np.sum(i) == 1:
                return True  # piece is placeed
            elif np.sum(i) == -1:
                return False  # piece is picked

    a = np.where(matrix != 0)
    rows = a[0]
    column = a[1]

    r, c = matrix.shape
    num = c - rows

    alp_notation = chr(97 + column[0])
    notation = alp_notation + str(num[0])

    action = get_sign(matrix)
    return [notation, action]


def getNotation(row_num, new_list):

    old_matrix = np.copy(new_matrix)  # Copy old matrix

    # print(old_matrix,'old')

    # newList=np.array(new_list)
    new_matrix[row_num] = new_list  # newList  # UPDATE THE NEW MATRIX WITH NEW ARRAY

    # print(new_matrix,'new')

    resultant_matrix = new_matrix - old_matrix  # Substract old matrix from new matrix
    # print(resultant_matrix,'result')
    ab = unit_matrix_to_notation(
        resultant_matrix
    )  # find position of 1 or -1 and its sign
    # ab=[<notation>,<sign>]

    return [ab[0], ab[1]]


def isNormalMove(move):
    if len(move) == 2:
        c1 = (move[0][1] == False) and (move[1][1] == True)

        return c1  # if condition is true then return true


def makeNormalMove(move):

    from_ = move[0][0]
    to = move[1][0]
    return from_ + to


def isCaptureMove(move):
    if len(move) == 3:  # condition 1 there should be three moves
        c2 = (move[0][1] == False) and (move[1][1] == False) and (move[2][1] == True)
        # condition 2 the action order of moves order should be pick , pick ,and  place
        case1 = move[0][0] == move[2][0]
        case2 = move[1][0] == move[2][0]
        # print(c1,c2,case1,case2)

        # condition 1 and 2 must be ture and either case1 or case2 should be true

        return c2 and (case1 or case2)


def makeCaptureMove(move):

    # refer notes to understand this
    # this function work as intended but it is complete mess
    if move[0][0] == move[2][0]:
        from_ = move[1][0]
        to = move[2][0]
    elif move[1][0] == move[2][0]:
        from_ = move[0][0]
        to = move[2][0]

    return from_ + to

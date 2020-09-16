# hardcoded testcases

# case 1
# nbr = [[0, 1, 1, 1, 1, 1, 1, 2, 2],
#         [0, 1, 1, 1, 1, 1, 1, 2, 2],
#         [0, 1, 1, 3, 3, 2, 2, 2, 2],
#         [0, 4, 4, 3, 3, 3, 2, 2, 2],
#         [4, 4, 4, 4, 4, 5, 5, 2, 2],
#         [4, 4, 4, 4, 4, 5, 5, 8, 8],
#         [6, 6, 4, 4, 7, 7, 5, 8, 8],
#         [6, 6, 6, 7, 7, 5, 5, 8, 8],
#         [6, 6, 6, 7, 7, 5, 5, 5, 8]
#         ]

# case 2
nbr = [[0, 0, 0, 0, 0, 1, 1, 2, 2],
        [3, 0, 0, 1, 1, 1, 2, 2, 2],
        [3, 4, 1, 1, 1, 2, 2, 2, 2],
        [3, 4, 4, 1, 1, 2, 2, 6, 6],
        [3, 4, 4, 1, 1, 2, 2, 6, 6],
        [4, 4, 4, 4, 5, 5, 5, 6, 6],
        [4, 4, 4, 7, 7, 7, 6, 6, 6],
        [4, 4, 7, 7, 7, 7, 8, 8, 8],
        [4, 4, 7, 7, 7, 7, 8, 8, 8]
        ]

import time

# function that checks if a given house can be placed at the given row, col given other variables
def isCorrect(configuration, row, col, num_in_rows, num_in_cols, num_in_nbrhoods):

    # basic check to see if row and column are even in range 
    if row < 0 or row >= 9:
        return False

    if col < 0 or col >= 9:
        return False

    # check if house on top
    if(row-1 >= 0):
        if configuration[row-1][col] == 1:
            return False

    # check if house on left
    if(col-1 >= 0):
        if configuration[row][col-1] == 1:
            return False

    # check if house on upper left diagonal
    if(row-1 >= 0 and col-1 >=0):
        if configuration[row-1][col-1] == 1:
            return False

    # check if house on lower left diagonal
    if(row+1 < 9 and col-1 >= 0):
        if configuration[row+1][col-1] == 1:
            return False

    # check for num houses in row
    if num_in_rows[row] > 1:
        return False

    # check for num houses in col
    if num_in_cols[col] > 1:
        return False

    # check for num houses in nbrhood
    if num_in_nbrhoods[nbr[row][col]] > 1:
        return False

    # if all the above is correct, return True
    return True



# function that defines problem and calls recursive solver
def solve_plan():

    num_in_rows = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_in_cols = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    num_in_nbrhoods = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    configuration = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]

    # recurses column by column                    
    isPossible = place_all_houses(configuration, num_in_rows, num_in_cols, num_in_nbrhoods, 0, 0) 
    print(isPossible)

    for i in range(len(configuration)):
        for j in range(len(configuration[i])):
            if configuration[i][j] == 1:
                print(i, j)


# function that recursively allots houses and checks if solution is correct
def place_all_houses(configuration, num_in_rows, num_in_cols, num_in_nbrhoods, curr_row, curr_col_to_fill):
    
    # base case, all cols filled
    if curr_col_to_fill >= 9:
        return True


    # recursively check all rows to be filled in this column
    for i in range(curr_row, 9):

        # if legal to allot this house
        if isCorrect(configuration, i, curr_col_to_fill, num_in_rows, num_in_cols, num_in_nbrhoods):

            # allot this house
            configuration[i][curr_col_to_fill] = 1
            # update all vars
            num_in_rows[i] += 1
            num_in_cols[curr_col_to_fill] += 1
            num_in_nbrhoods[nbr[i][curr_col_to_fill]] += 1

            # first find next column and next row
            next_row = None
            next_col = None
            if num_in_cols[curr_col_to_fill] < 2 :
                next_col = curr_col_to_fill
                next_row = i+1
            else :
                next_col = curr_col_to_fill + 1
                next_row = 0

            # # DEBUG PRINT STATEMENT
            # print("Just placed")    
            # for row_tp in configuration:
            #     for elem_tp in row_tp:
            #         if elem_tp == 0:
            #             print("o", end=" ")
            #         else :
            #             print("X", end=" ")
            #     print()
            # print("------------------")
            # time.sleep(5)

            # recur to allot next house, which must go in at least the next row
            if place_all_houses(configuration, num_in_rows, num_in_cols, num_in_nbrhoods, next_row, next_col) == True:
                return True


            # if this didn't work un-allot this house
            configuration[i][curr_col_to_fill] = 0
            # reset all vars
            num_in_rows[i] -= 1
            num_in_cols[curr_col_to_fill] -= 1
            num_in_nbrhoods[nbr[i][curr_col_to_fill]] -= 1

    # if it couldn't be allotted anywhere in the column return False
    return False


solve_plan()
# Authour: Samantha Preisig
# Purpose: Contains various fixed win conditions

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the board (with all plays marked)
#   @param int size: the size of the board (3 = 3x3, 4 = 4x4, 5 = 5x5)
#   @param char letter: X or O
#   @return True if letter has completed a row on the board, False otherwise
def has_row(board, size, letter):
    # Row win conditions for 3x3 TTT board
    if(size == 3):
        if(board[1] == board[2] and board[1] == board[3] and board[1] == letter):
            return True
        elif(board[4] == board[5] and board[4] == board[6] and board[4] == letter):
            return True
        elif(board[7] == board[8] and board[7] == board[9] and board[9] == letter):
            return True
        else:
            return False

    # Row win conditions for 4x4 TTT board
    if(size == 4):
        if(board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == letter):
            return True
        elif(board[5] == board[6] and board[5] == board[7] and board[5] == board[8] and board[5] == letter):
            return True
        elif(board[9] == board[10] and board[9] == board[11] and board[9] == board[12] and board[9] == letter):
            return True
        elif(board[13] == board[14] and board[13] == board[15] and board[13] == board[16] and board[13] == letter):
            return True
        else:
            return False

    # Row win conditions for 5x5 TTT board
    if(size == 5):
        if(board[1] == board[2] and board[1] == board[3] and board[1] == board[4] and board[1] == board[5] and board[1] == letter):
            return True
        elif(board[6] == board[7] and board[6] == board[8] and board[6] == board[9] and board[6] == board[10] and board[6] == letter):
            return True
        elif(board[11] == board[12] and board[11] == board[13] and board[11] == board[14] and board[11] == board[15] and board[11] == letter):
            return True
        elif(board[16] == board[17] and board[16] == board[18] and board[16] == board[19] and board[16] == board[20] and board[16] == letter):
            return True
        elif(board[21] == board[22] and board[21] == board[23] and board[21] == board[24] and board[21] == board[25] and board[21] == letter):
            return True
        else:
            return False

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the board (with all plays marked)
#   @param int size: the size of the board (3 = 3x3, 4 = 4x4, 5 = 5x5)
#   @param char letter: X or O
#   @return True if letter has completed a row on the board, False otherwise
def has_col(board, size, letter):
    # Column win conditions for 3x3 TTT board
    if(size == 3):
        if(board[1] == board[4] and board[1] == board[7] and board[1] == letter):
            return True
        elif(board[2] == board[5] and board[2] == board[8] and board[2] == letter):
            return True
        elif(board[3] == board[6] and board[3] == board[9] and board[3] == letter):
            return True
        else:
            return False

    # Column win conditions for 4x4 TTT board
    if(size == 4):
        if(board[1] == board[5] and board[1] == board[9] and board[1] == board[13] and board[1] == letter):
            return True
        elif(board[2] == board[6] and board[2] == board[10] and board[2] == board[14] and board[2] == letter):
            return True
        elif(board[3] == board[7] and board[3] == board[11] and board[3] == board[15] and board[3] == letter):
            return True
        elif(board[4] == board[8] and board[4] == board[12] and board[4] == board[16] and board[4] == letter):
            return True
        else:
            return False

    # Column win conditions for 5x5 TTT board
    if(size == 5):
        if(board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == board[21] and board[1] == letter):
            return True
        elif(board[2] == board[7] and board[2] == board[12] and board[2] == board[17] and board[2] == board[22] and board[2] == letter):
            return True
        elif(board[3] == board[8] and board[3] == board[13] and board[3] == board[18] and board[3] == board[23] and board[3] == letter):
            return True
        elif(board[4] == board[9] and board[4] == board[14] and board[4] == board[19] and board[4] == board[24] and board[4] == letter):
            return True
        elif(board[5] == board[10] and board[5] == board[15] and board[5] == board[20] and board[5] == board[25] and board[5] == letter):
            return True
        return False

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the board (with all plays marked)
#   @param int size: the size of the board (3 = 3x3, 4 = 4x4, 5 = 5x5)
#   @param char letter: X or O
#   @return True if letter has completed a row on the board, False otherwise
def has_diag(board, size, letter):
    # Diagonal win conditions for 3x3 TTT board
    if(size == 3):
        if(board[1] == board[5] and board[1] == board[9] and board[1] == letter):
            return True
        elif(board[7] == board[5] and board[7] == board[3] and board[7] == letter):
            return True
        else:
            return False

    # Diagonal win conditions for 4x4 TTT board
    if(size == 4):
        if(board[1] == board[6] and board[1] == board[11] and board[1] == board[16] and board[1] == letter):
            return True
        elif(board[13] == board[4] and board[13] == board[7] and board[13] == board[10] and board[13] == letter):
            return True
        else:
            return False

    # Diagonal win conditions for 5x5 TTT board
    if(size == 5):
        if(board[1] == board[7] and board[1] == board[13] and board[1] == board[19] and board[1] == board[25] and board[1] == letter):
            return True
        elif(board[21] == board[17] and board[21] == board[13] and board[21] == board[9] and board[21] == board[5] and board[21] == letter):
            return True
        else:
            return False

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the 4x4 board (with all plays marked)
#   @param char letter: X or O
#   @return True if letter has completed a row on the 4x4 board, False otherwise
def has_square(board, letter):
    # Only applies to 4x4 TTT board
    if(board[1] == board[2] and board[1] == board[5] and board[1] == board[6] and board[1] == letter):
        return True
    elif(board[2] == board[3] and board[2] == board[6] and board[2] == board[7] and board[2] == letter):
        return True
    elif(board[3] == board[4] and board[3] == board[7] and board[3] == board[8] and board[3] == letter):
        return True
    elif(board[5] == board[6] and board[5] == board[9] and board[5] == board[10] and board[5] == letter):
        return True
    elif(board[6] == board[7] and board[6] == board[10] and board[6] == board[11] and board[6] == letter):
        return True
    elif(board[7] == board[8] and board[7] == board[11] and board[7] == board[12] and board[7] == letter):
        return True
    elif(board[9] == board[10] and board[9] == board[13] and board[9] == board[14] and board[9] == letter):
        return True
    elif(board[10] == board[11] and board[10] == board[14] and board[10] == board[15] and board[10] == letter):
        return True
    elif(board[11] == board[12] and board[11] == board[15] and board[11] == board[16] and board[11] == letter):
        return True
    else:
        return False

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the 4x4 board (with all plays marked)
#   @param char letter: X or O
#   @return True if letter has completed a row on the 4x4 board, False otherwise
def has_diamond(board, letter):
    # Only applies to 4x4 TTT board
    if(board[2] == board[5] and board[2] == board[7] and board[2] == board[10] and board[2] == letter):
        return True
    elif(board[3] == board[6] and board[3] == board[8] and board[3] == board[11] and board[3] == letter):
        return True
    elif(board[6] == board[9] and board[6] == board[11] and board[6] == board[14] and board[6] == letter):
        return True
    elif(board[7] == board[10] and board[7] == board[12] and board[7] == board[15] and board[7] == letter):
        return True
    else:
        return False

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the 5x5 board (with all plays marked)
#   @param int size: the size of the board (3 = 3x3, 4 = 4x4, 5 = 5x5)
#   @param char letter: X or O
#   @return True if letter has completed a row on the 5x5 board, False otherwise
def has_plus(board, letter):
    # Only applies to 5x5 TTT board
    if(board[2] == board[6] and board[2] == board[7] and board[2] == board[8] and board[2] == board[12] and board[2] == letter):
        return True
    elif(board[3] == board[7] and board[3] == board[8] and board[3] == board[9] and board[3] == board[13] and board[3] == letter):
        return True
    elif(board[4] == board[8] and board[4] == board[9] and board[4] == board[10] and board[4] == board[14] and board[4] == letter):
        return True
    elif(board[7] == board[11] and board[7] == board[12] and board[7] == board[13] and board[7] == board[17] and board[7] == letter):
        return True
    elif(board[8] == board[12] and board[8] == board[13] and board[8] == board[14] and board[8] == board[18] and board[8] == letter):
        return True
    elif(board[9] == board[13] and board[9] == board[14] and board[9] == board[15] and board[9] == board[19] and board[9] == letter):
        return True
    elif(board[12] == board[16] and board[12] == board[17] and board[12] == board[18] and board[12] == board[22] and board[12] == letter):
        return True
    elif(board[13] == board[17] and board[13] == board[18] and board[13] == board[19] and board[13] == board[23] and board[13] == letter):
        return True
    elif(board[14] == board[18] and board[14] == board[19] and board[14] == board[20] and board[14] == board[24] and board[14] == letter):
        return True
    else:
        return False

# Checks if a row has been completed (a win has been achieved)
#   @param int board: the current matrix of the 5x5 board (with all plays marked)
#   @param int size: the size of the board (3 = 3x3, 4 = 4x4, 5 = 5x5)
#   @param char letter: X or O
#   @return True if letter has completed a row on the 5x5 board, False otherwise
def has_L(board, letter):
    # Only applies to 5x5 TTT board
    # L win conditions
    if(board[1] == board[6] and board[1] == board[11] and board[1] == board[12] and board[1] == board[13] and board[1] == letter):
        return True
    elif(board[2] == board[7] and board[2] == board[12] and board[2] == board[13] and board[2] == board[14] and board[2] == letter):
        return True
    elif(board[3] == board[8] and board[3] == board[13] and board[3] == board[14] and board[3] == board[15] and board[3] == letter):
        return True
    elif(board[6] == board[11] and board[6] == board[16] and board[6] == board[17] and board[6] == board[18] and board[6] == letter):
        return True
    elif(board[7] == board[12] and board[7] == board[17] and board[7] == board[18] and board[7] == board[19] and board[7] == letter):
        return True
    elif(board[8] == board[13] and board[8] == board[18] and board[8] == board[19] and board[8] == board[20] and board[8] == letter):
        return True
    elif(board[11] == board[16] and board[11] == board[21] and board[11] == board[22] and board[11] == board[23] and board[11] == letter):
        return True
    elif(board[12] == board[17] and board[12] == board[22] and board[12] == board[23] and board[12] == board[24] and board[12] == letter):
        return True
    elif(board[13] == board[18] and board[13] == board[23] and board[13] == board[24] and board[13] == board[25] and board[13] == letter):
        return True

    # L rotated 90 degrees to the right
    elif(board[1] == board[2] and board[1] == board[3] and board[1] == board[6] and board[1] == board[11] and board[1] == letter):
        return True
    elif(board[2] == board[3] and board[2] == board[4] and board[2] == board[7] and board[2] == board[12] and board[2] == letter):
        return True
    elif(board[3] == board[4] and board[3] == board[5] and board[3] == board[8] and board[3] == board[13] and board[3] == letter):
        return True
    elif(board[6] == board[7] and board[6] == board[8] and board[6] == board[11] and board[6] == board[16] and board[6] == letter):
        return True
    elif(board[7] == board[8] and board[7] == board[9] and board[7] == board[12] and board[7] == board[17] and board[7] == letter):
        return True
    elif(board[8] == board[9] and board[8] == board[10] and board[8] == board[13] and board[8] == board[18] and board[8] == letter):
        return True
    elif(board[11] == board[12] and board[11] == board[13] and board[11] == board[16] and board[11] == board[21] and board[11] == letter):
        return True
    elif(board[12] == board[13] and board[12] == board[14] and board[12] == board[17] and board[12] == board[22] and board[12] == letter):
        return True
    elif(board[13] == board[14] and board[13] == board[15] and board[13] == board[18] and board[13] == board[23] and board[13] == letter):
        return True

    # L rotated 180 degrees to the right
    elif(board[1] == board[2] and board[1] == board[3] and board[1] == board[8] and board[1] == board[13] and board[1] == letter):
        return True
    elif(board[2] == board[3] and board[2] == board[4] and board[2] == board[9] and board[2] == board[14] and board[2] == letter):
        return True
    elif(board[3] == board[4] and board[3] == board[5] and board[3] == board[10] and board[3] == board[15] and board[3] == letter):
        return True
    elif(board[6] == board[7] and board[6] == board[8] and board[6] == board[13] and board[6] == board[18] and board[6] == letter):
        return True
    elif(board[7] == board[8] and board[7] == board[9] and board[7] == board[14] and board[7] == board[19] and board[7] == letter):
        return True
    elif(board[8] == board[9] and board[8] == board[10] and board[8] == board[15] and board[8] == board[20] and board[8] == letter):
        return True
    elif(board[11] == board[12] and board[11] == board[13] and board[11] == board[18] and board[11] == board[23] and board[11] == letter):
        return True
    elif(board[12] == board[13] and board[12] == board[14] and board[12] == board[19] and board[12] == board[24] and board[12] == letter):
        return True
    elif(board[13] == board[14] and board[13] == board[15] and board[13] == board[20] and board[13] == board[25] and board[13] == letter):
        return True
    
    # L rotated 270 degrees to the right
    elif(board[3] == board[8] and board[3] == board[11] and board[3] == board[12] and board[3] == board[13] and board[3] == letter):
        return True
    elif(board[4] == board[9] and board[4] == board[12] and board[4] == board[13] and board[4] == board[14] and board[4] == letter):
        return True
    elif(board[5] == board[10] and board[5] == board[13] and board[5] == board[14] and board[5] == board[15] and board[5] == letter):
        return True
    elif(board[8] == board[13] and board[8] == board[16] and board[8] == board[17] and board[8] == board[18] and board[8] == letter):
        return True
    elif(board[9] == board[14] and board[9] == board[17] and board[9] == board[18] and board[9] == board[19] and board[9] == letter):
        return True
    elif(board[10] == board[15] and board[10] == board[18] and board[10] == board[19] and board[10] == board[20] and board[10] == letter):
        return True
    elif(board[13] == board[18] and board[13] == board[21] and board[13] == board[22] and board[13] == board[23] and board[13] == letter):
        return True
    elif(board[14] == board[19] and board[14] == board[22] and board[14] == board[23] and board[14] == board[24] and board[14] == letter):
        return True
    elif(board[15] == board[20] and board[15] == board[23] and board[15] == board[24] and board[15] == board[25] and board[15] == letter):
        return True
    else:
        return False
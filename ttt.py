import time
from win_conditions import has_row, has_col, has_diag, has_square, has_diamond, has_plus, has_L

### GLOBAL VARIABLES ###
PLAYER = 'X'
BOT = 'O'
TIMEOUT_THRESHOLD = 60000000000 # 60000000000ns = 60s = 1min
timeout = False
start_time = 0
size = 0
board = {}
alpha_beta_chosen = False
prev_utility = -2 # Stores the last result of minimax (fall back on prev_utility when TIMEOUT_THRESHOLD is reached)
nodes_explored = 0
search_depth_reached = -1

### HELPER FUNCTIONS ###
def print_game(board, size):
    if(size == 3):
        print(board[1] + '|' + board[2] + '|' + board[3])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[7] + '|' + board[8] + '|' + board[9])
        print("\n")
    
    elif(size == 4):
        print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4])
        print('-+-+-+-')
        print(board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8])
        print('-+-+-+-')
        print(board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12])
        print('-+-+-+-')
        print(board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16])
        print("\n")

    elif(size == 5):
        print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5])
        print('-+-+-+-+-')
        print(board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10])
        print('-+-+-+-+-')
        print(board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14] + '|' + board[15])
        print('-+-+-+-+-')
        print(board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20])
        print('-+-+-+-+-')
        print(board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25])
        print("\n")

def open_position(pos):
    if(board[pos] == ' '):
        return True
    else:
        return False

def game_won(board, size, letter):
    if has_row(board, size, letter):
        return True
    if has_col(board, size, letter):
        return True
    if has_diag(board, size, letter):
        return True
    
    if(size == 4):
        if has_square(board, letter):
            return True
        if has_diamond(board, letter):
            return True
    if(size == 5):
        if has_plus(board, letter):
            return True
        if has_L(board, letter):
            return True
    return False

def check_draw():
    for key in board.keys():
        if(board[key] == ' '):
            return False
    return True

def play_position(letter, pos, max_ply):
    if open_position(pos):
        board[pos] = letter
        print_game(board, size)

        if(letter == BOT):
            if timeout:
                print("[Bot] Time taken to decide and make move: ~1 minute (TIMED OUT)")
            else:
                print("[Bot] Time taken to decide and make move: " + str((time.perf_counter_ns()-start_time)/1000000) + "ms")
            print("[Bot] Nodes explored: ", nodes_explored)
            print("[Bot] Search depth reached: " + str(max_ply-search_depth_reached) + "\n")

        if game_won(board, size, PLAYER):
            print("Human won")
            return
        elif game_won(board, size, BOT):
            print("Bot won")
            return
        if check_draw():
            print("DRAW")
            return
    else:
        print("Cannot play that position.")
        pos = int(input("Please enter another position: "))
        play_position(letter, pos, max_ply)

def player_move(max_ply):
    pos = int(input("Enter the position for 'X': "))
    play_position(PLAYER, pos, max_ply)

def bot_move(max_ply):
    global start_time, timeout
    # Checking if player won or drew before proceeding
    if(game_won(board, size, PLAYER) or check_draw()):
        return

    timeout = False
    start_time = time.perf_counter_ns()
    # for depth in range(0, max_ply):
    best_score = -1000
    best_move = 0

    for key in board.keys():
        if(board[key] == ' '):
            board[key] = BOT

            if alpha_beta_chosen:
                score = alpha_beta(board, max_ply, -1000, 1000, False) # score = alpha_beta(board, depth, -1000, 1000, False)
            else:
                score = minimax(board, max_ply, False) # score = minimax(board, depth, False)
            
            board[key] = ' '
            if(score > best_score):
                best_score = score
                best_move = key
        if timeout:
            break
    play_position(BOT, best_move, max_ply)

def max(val_1, val_2):
    if(val_1 >= val_2):
        return val_1
    else:
        return val_2

def min(val_1, val_2):
    if(val_1 <= val_2):
        return val_1
    else:
        return val_2

def minimax(board, depth, maximizing_player):
    global prev_utility, start_time, timeout, nodes_explored, search_depth_reached
    
    if((time.perf_counter_ns()-start_time) > TIMEOUT_THRESHOLD):
        timeout = True
        return prev_utility
    if game_won(board, size, BOT):
        return 1
    elif game_won(board, size, PLAYER):
        return -1
    elif check_draw():
        return 0
    if(depth < 0):
        return -2
    
    search_depth_reached = depth
    nodes_explored += 1
    if maximizing_player:
        max_eval = -1000
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = BOT
                eval = minimax(board, depth-1, False)
                board[key] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 1000
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = PLAYER
                eval = minimax(board, depth-1, True)
                board[key] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    global prev_utility, start_time, timeout, nodes_explored, search_depth_reached
    
    if((time.perf_counter_ns()-start_time) > TIMEOUT_THRESHOLD):
        timeout = True
        return prev_utility
    if game_won(board, size, BOT):
        return 1
    elif game_won(board, size, PLAYER):
        return -1
    elif check_draw():
        return 0
    if(depth < 0):
        return -2
    
    search_depth_reached = depth
    nodes_explored += 1
    if maximizing_player:
        max_eval = -1000
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = BOT
                eval = alpha_beta(board, depth-1, alpha, beta, False)
                board[key] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if(beta <= alpha):
                    break
                prev_utility = max_eval
        return max_eval
    else:
        min_eval = 1000
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = PLAYER
                eval = alpha_beta(board, depth-1, alpha, beta, True)
                board[key] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if(beta <= alpha):
                    break
                prev_utility = min_eval
        return min_eval

### DRIVER ###
def main():
    global size, board, alpha_beta_chosen, nodes_explored, search_depth_reached

    print("Welcome to Tic-Tac-Toe!\n")

    # User selects board size (3x3, 4x4, or 5x5)
    size = int(input("Please enter size of Tic-Tac-Toe board [3, 4, or 5]: "))
    while(not(size == 3 or size == 4 or size == 5)):
        size = int(input("Size not implemeted. Please enter size of Tic-Tac-Toe board [3, 4, or 5]: "))
    if(size == 3):
        board = {
            1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '
        }
    elif(size == 4):
        board = {
            1: ' ', 2: ' ', 3: ' ', 4: ' ',
            5: ' ', 6: ' ', 7: ' ', 8: ' ',
            9: ' ', 10: ' ', 11: ' ', 12: ' ',
            13: ' ', 14: ' ', 15: ' ', 16: ' '
        }
    elif(size == 5):
        board = {
            1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ',
            6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ',
            11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ',
            16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ',
            21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' '
        }
    
    # User selects what algorithm the bot uses (minimax or alpha-beta)
    algo = str(input("How do you want the bot to play? [m = minimax, a = alpha-beta]: "))
    while(not(algo == 'm' or algo == 'a')):
        algo = str(input("Please chose an algorithm for bot [m = minimax, a = alpha-beta]: "))
    if(algo == 'a'):
        alpha_beta_chosen = True
    else:
        alpha_beta_chosen = False
    
    # User selects maximum ply
    max_ply = int(input("Enter maximum ply: "))
    print("\n")
    
    print_game(board, size)
    while not (game_won(board, size, PLAYER) or game_won(board, size, BOT) or check_draw()):
        player_move(max_ply)
        nodes_explored = 0
        search_depth_reached = 0
        bot_move(max_ply)

if __name__ == "__main__":
    main()

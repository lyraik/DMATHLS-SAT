from itertools import combinations

def is_valid_board_strict(board):
    """
    Check if the board is valid under strict conditions:
    - Exactly one winning combination for X
    - No winning combination for O
    - All spaces are filled
    """
    winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    x_wins_count = 0

    for combo in winning_combinations:
        if all(board[pos] == 'X' for pos in combo):
            x_wins_count += 1
        if all(board[pos] == 'O' for pos in combo):
            return False  # O wins, invalid

    return x_wins_count == 1  # Exactly one win for X

def count_valid_boards_strict():
    #Count the number of valid boards under strict conditions.
    
    positions = range(9)
    count = 0

    # X always wins in 5 moves, so combinations of 5 X's and 4 O's are considered
    for x_positions in combinations(positions, 5):
        for o_positions in combinations(positions, 4):
            if set(x_positions).isdisjoint(o_positions):  # Ensure X and O are in different positions
                board = [' '] * 9
                for pos in x_positions:
                    board[pos] = 'X'
                for pos in o_positions:
                    board[pos] = 'O'
                if is_valid_board_strict(board):
                    count += 1

    return count

valid_boards_count_strict = count_valid_boards_strict()
print(valid_boards_count_strict)

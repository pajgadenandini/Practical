def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check the current column for another queen
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Recursive Backtracking Solution
def solve_queens_recursive(board, row):
    if row >= len(board):
        return True  # Solution found

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_queens_recursive(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False  # No solution found in this configuration

# Iterative Backtracking Solution
def solve_queens_iterative(board):
    n = len(board)
    row, col = 1, 0  # Start from the second row since first queen is already placed
    stack = [(0, 0)]  # Initial queen position in (0,0)

    while row < n:
        placed = False
        while col < n:
            if is_safe(board, row, col):
                # Place queen and move to the next row
                board[row][col] = 1
                stack.append((row, col))
                row += 1
                col = 0  # Reset column for the new row
                placed = True
                break
            col += 1

        if not placed:
            # Backtrack if no valid column is found
            if not stack:
                return False  # No solution if stack is empty

            # Remove last placed queen
            row, col = stack.pop()
            board[row][col] = 0  # Unmark last queen position
            col += 1  # Try next column in the same row

    return True  # Solution found

def solve_8_queens(use_recursive=True):
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1  # Place the first queen at (0,0)

    if use_recursive:
        print("Solving using Recursive Backtracking...")
        solve_queens_recursive(board, 1)
    else:
        print("Solving using Iterative Backtracking...")
        solve_queens_iterative(board)

    print("Final Board Configuration:")
    print_board(board)

# Run the solution for both recursive and iterative
solve_8_queens(use_recursive=True)
solve_8_queens(use_recursive=False)


















# Worst-case Time Complexity: 
# 𝑂(𝑛!)O(n!)
# This is because, in the worst case, we may need to explore all possible arrangements of 

# n queens on an n×n board.
# Specifically, for each row, there are up to 𝑛
# n possible placements, and we recursively try placing queens in each row until we find a solution or backtrack.
# This is an exponential complexity, making the problem very computationally intensive for large 
# n.

# Recursive Backtracking: 
# 𝑂
# (
# 𝑛
# )
# O(n) for the recursive call stack.

# Each recursive call goes one level deeper until reaching 
# 𝑛
# n levels for an 
# 𝑛
# n-Queens board, so the space required is proportional to 
# 𝑛
# n.
# Iterative Backtracking with Stack: 
# 𝑂
# (
# 𝑛
# )
# O(n) for the stack used to store queen positions.

# In the iterative approach, we also store queen positions in a stack with up to 
# 𝑛
# n elements, requiring 
# 𝑂
# (
# 𝑛
# )
# O(n) space.
# Cryptography and Cybersecurity
# Parallel Computing:

# Since the N-Queens problem can be broken down into independent subproblems (each row can be solved independently before being checked for consistency), it serves as a teaching tool for parallel algorithms and distributed computing setups.
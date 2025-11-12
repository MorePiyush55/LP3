def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - row + i >= 0 and board[i][col - row + i] == 1) or \
           (col + row - i < n and board[i][col + row - i] == 1):
            return False
    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0

def n_queens():
    n = int(input("Enter N: "))
    board = [[0]*n for _ in range(n)]
    r, c = map(int, input("Enter first queen position (row col): ").split())
    board[r-1][c-1] = 1
    print("\nInitial board:")
    print_board(board)
    print("Solutions:\n")
    solve(board, 0, n)

if __name__ == "__main__":
    n_queens()

# Output:
# Enter N: 4
# Enter first queen position (row col): 1 2

####################################################################

🧾 1. Short Summary

This Python program solves the N-Queens problem using backtracking.
The objective is to place N queens on an N×N chessboard such that no two queens attack each other — meaning no two queens share the same row, column, or diagonal.

📘 2. Theory
➤ What is the N-Queens Problem?

You must place N queens on a chessboard so that none threaten each other.

Queens attack in all 8 directions — horizontally, vertically, and diagonally.

The challenge is to find all possible arrangements that satisfy this condition.

➤ Backtracking Concept

Backtracking is a trial-and-error search algorithm that tries all possible configurations recursively.

If a move leads to a conflict, it “backtracks” and tries the next possibility.

It is a form of depth-first search in solution space.

⚙️ 3. Algorithm (Step-by-Step)

Input N (size of the board).

Initialize an N×N matrix board with zeros.

Place the first queen at the given position.

Try placing the next queen in the next row:

Check if the position is safe using is_safe().

If safe, place the queen (set 1) and recursively place the next queen.

If not safe, backtrack (remove the queen and try another column).

Repeat until all queens are placed.

Print all valid configurations.

🧩 4. Key Concepts Used
Concept	Explanation
Backtracking	Systematically searches for all possible solutions by exploring and undoing moves.
Recursion	Calls itself to place the next queen after placing the current one.
2D Array (Matrix)	Represents the chessboard (0 = empty, 1 = queen).
is_safe() Function	Checks if placing a queen at (row, col) is conflict-free.
Constraint Checking	Ensures no two queens share same column or diagonals.
Base Case	When row == n, all queens are placed successfully — print the board.


✅ Two valid solutions exist for N = 4.

⏱️ 7. Complexity Analysis
Type	Complexity	Description
Time Complexity	O(N!)	Tries all possible column positions for each queen.
Space Complexity	O(N²)	For storing the chessboard.
🎯 8. Conclusion

This program uses the backtracking algorithm to solve the N-Queens problem efficiently.
It explores all valid queen placements recursively and backtracks upon conflict.
This is a classic example of constraint satisfaction and recursion-based search in AI and algorithm design.

🎤 9. Top 10 Viva Questions & Answers
No.	Question	Answer
1	What is the N-Queens problem?	Placing N queens on an N×N chessboard so that none attack each other.
2	Which algorithm is used here?	Backtracking algorithm.
3	What is backtracking?	It’s a recursive trial-and-error approach that undoes wrong choices.
4	What is the base condition in this program?	When all rows are filled (row == n).
5	Why can’t two queens be in the same diagonal?	Because they would attack each other diagonally.
6	What does the function is_safe() check?	Ensures no queen in same column or diagonals.
7	What data structure is used for the board?	2D list (matrix).
8	What is the time complexity?	O(N!).
9	What is printed when a valid arrangement is found?	The board configuration with 1s representing queens.
10	Real-life applications?	Solving scheduling problems, puzzles, and constraint satisfaction tasks.
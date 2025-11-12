import time

# ---------- Recursive Fibonacci ----------
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# ---------- Non-Recursive Fibonacci ----------
def fib_non_recursive(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()

# ---------- Main Function ----------
def main():
    n = int(input("Enter the number of elements: "))

    print("\nFibonacci Sequence (Recursive): ", end="")
    start1 = time.time()
    for i in range(n):
        print(fib_recursive(i), end=" ")
    end1 = time.time()
    time_recursive = (end1 - start1) * 1_000_000  # microseconds

    print("\n\nFibonacci Sequence (Non-Recursive): ", end="")
    start2 = time.time()
    fib_non_recursive(n)
    end2 = time.time()
    time_nonrecursive = (end2 - start2) * 1_000_000  # microseconds

    # ---------- Time & Space Complexity ----------
    print("\n=== Time and Space Complexity Analysis ===")
    print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
    print("Recursive Time Complexity: O(2^n)")
    print("Recursive Space Complexity: O(n)\n")

    print(f"Non-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
    print("Non-Recursive Time Complexity: O(n)")
    print("Non-Recursive Space Complexity: O(1)")

if __name__ == "__main__":
    main()


***************************************

1. Short Summary

This program generates the Fibonacci series using both recursion and iteration (non-recursive).
It compares their execution time, time complexity, and space complexity to show how recursion is slower and uses more memory.

📘 2. Theory
➤ Fibonacci Series

A sequence where each number is the sum of the two preceding ones.
Formula:
F(n) = F(n−1) + F(n−2)
Starting values:
F(0) = 0, F(1) = 1

Example:
0, 1, 1, 2, 3, 5, 8, 13, …

➤ Recursive Function

A function that calls itself until a base condition is reached.
In this case, fib_recursive(n) calls itself twice per call → exponential growth.

➤ Non-Recursive (Iterative)

Uses loops to calculate the next term step-by-step, storing only the last two numbers.
Much faster and uses less memory.

⚙️ 3. Algorithm
Recursive Fibonacci

Input n.

If n <= 1, return n.

Else, return fib_recursive(n-1) + fib_recursive(n-2).

Repeat until all terms are printed.

Non-Recursive Fibonacci

Input n.

Initialize n1 = 0, n2 = 1.

Print first two numbers.

Loop from 2 to n−1:

n3 = n1 + n2

Print n3

Update: n1 = n2, n2 = n3

Stop when n terms are printed.

🧩 4. Key Concepts Used
Concept	Explanation
Recursion	Function calling itself for smaller subproblems until a base case.
Iteration	Uses loops to repeatedly execute code until a condition fails.
Time Module	Used to record start and end time for both methods.
Time Complexity	Recursive → O(2ⁿ), Iterative → O(n).
Space Complexity	Recursive → O(n) due to function call stack, Iterative → O(1).
Base Condition	Stops infinite recursion (if n <= 1: return n).
Loop	For loop runs n−2 times to generate sequence.
🧮 5. Complexity Analysis
Method	Time Complexity	Space Complexity	Speed	Remarks
Recursive	O(2ⁿ)	O(n)	Slow	Recomputes many values
Non-Recursive	O(n)	O(1)	Fast	Efficient and memory-friendly

| No. | Question                                             | Answer                                                                         |
| --- | ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1   | What is the Fibonacci series?                        | A sequence where each number is the sum of the previous two numbers.           |
| 2   | What is recursion?                                   | A method where a function calls itself until a base case is reached.           |
| 3   | What is the base condition in this program?          | When `n <= 1`, the function returns `n`.                                       |
| 4   | Why is recursion slower here?                        | Because it recomputes the same values multiple times, giving exponential time. |
| 5   | What is the time complexity of recursive Fibonacci?  | O(2ⁿ).                                                                         |
| 6   | What is the time complexity of iterative Fibonacci?  | O(n).                                                                          |
| 7   | What is the space complexity of recursive Fibonacci? | O(n) due to recursive call stack.                                              |
| 8   | What is the advantage of iteration?                  | Faster and uses less memory.                                                   |
| 9   | Why is `time` module used?                           | To measure and compare execution time of both methods.                         |
| 10  | Which approach is better and why?                    | Iterative — it’s faster and memory-efficient.                                  |

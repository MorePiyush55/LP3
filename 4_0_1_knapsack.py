def knapsack_dp():
    # Step 1: Take user input
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    print("\nEnter weight and value (profit) for each item separated by space:")
    for i in range(n):
        w, v = map(int, input(f"Item {i+1}: ").split())
        weights.append(w)
        values.append(v)

    W = int(input("\nEnter maximum capacity of knapsack: "))

    # Step 2: Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 3: Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 4: Output result
    print("\n Maximum profit that can be obtained:", dp[n][W])


if __name__ == "__main__":
    knapsack_dp()

# output:

# Enter number of items: 3
# Enter weight and value (profit) for each item separated by space:
# Item 1: 10 60
# Item 2: 20 110
# Item 3: 30 150

# Enter maximum capacity of knapsack: 50

#  Maximum profit that can be obtained: 260

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4

1. Short Summary

This Python program implements the 0/1 Knapsack problem using Dynamic Programming (DP).
The goal is to find the maximum profit/value that can be obtained by selecting items such that their total weight doesn’t exceed the knapsack’s capacity — each item can be taken either completely or not at all (no fractions).

📘 2. Theory
➤ Knapsack Problem

Given:

n items, each with weight (w[i]) and value (v[i])

A knapsack with maximum capacity W

Find the maximum total value of items that can be included in the knapsack without exceeding capacity.

➤ 0/1 Knapsack Type

Each item can either be included (1) or excluded (0) — no partial selection.

Solved efficiently using Dynamic Programming (unlike the greedy method, which doesn’t guarantee optimality here).

⚙️ 3. Algorithm (Dynamic Programming Approach)

Input n items and their respective weights and values.

Input the maximum capacity W of the knapsack.

Create a 2D table dp[n+1][W+1], where each cell dp[i][w] stores the maximum profit for the first i items and capacity w.

Fill the DP table:

For each item i and capacity w:

If weights[i-1] <= w
→ include = values[i-1] + dp[i-1][w - weights[i-1]]
→ exclude = dp[i-1][w]
→ dp[i][w] = max(include, exclude)

Else
→ dp[i][w] = dp[i-1][w]

The final answer is stored in dp[n][W].

🧩 4. Key Concepts Used
Concept	Explanation
Dynamic Programming (DP)	Breaks problem into smaller overlapping subproblems and stores results to avoid recomputation.
Tabulation (Bottom-Up)	DP table is filled iteratively from smallest subproblems to final solution.
2D Array	Stores max profit for every item-capacity combination.
Optimal Substructure	Solution depends on results of smaller subproblems.
Overlapping Subproblems	Same subproblems appear repeatedly; DP saves their results.


✅ Explanation:

Select item 2 (20, 110) and item 3 (30, 150) → total = 260 (fits exactly into 50).

⏱️ 7. Complexity Analysis
Type	Complexity	Description
Time Complexity	O(n × W)	Each cell in DP table is computed once.
Space Complexity	O(n × W)	For storing DP table.
🎯 8. Conclusion

This program demonstrates how Dynamic Programming efficiently solves the 0/1 Knapsack problem by storing intermediate results in a table.
Unlike the Fractional Knapsack (Greedy), this ensures an optimal solution even when fractional selection is not allowed.

🎤 9. Top 10 Viva Questions & Answers
No.	Question	Answer
1	What is the 0/1 Knapsack problem?	Select items to maximize value without exceeding capacity; take an item fully or not at all.
2	Which algorithm is used here?	Dynamic Programming (Bottom-Up approach).
3	Why can’t we use the greedy method here?	Greedy may not always give the optimal solution in 0/1 case.
4	What does dp[i][w] represent?	Max profit with first i items and capacity w.
5	What is the time complexity?	O(n × W).
6	What is the space complexity?	O(n × W).
7	What are overlapping subproblems?	Subproblems that repeat during computation — solved once and reused.
8	What is the difference between 0/1 and Fractional Knapsack?	Fractional allows partial items; 0/1 doesn’t.
9	What approach is used in this program?	Bottom-up Dynamic Programming (Tabulation).
10	What is the base case in DP table?	If i = 0 or W = 0, profit = 0.
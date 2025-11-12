def fractional_knapsack():
    # Step 1: Take number of items
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    # Step 2: Take weight and value together on same line
    print("\nEnter weight and value for each item (separated by space):")
    for i in range(n):
        w, v = map(float, input(f"Item {i+1}: ").split())
        weights.append(w)
        values.append(v)

    # Step 3: Take knapsack capacity
    capacity = float(input("\nEnter knapsack capacity: "))

    # Step 4: Fractional knapsack logic
    res = 0.0
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)

    print("\nItem selection process:")
    for weight, value in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            res += value
            capacity -= weight
            print(f"  Took full item (weight={weight}, value={value})")
        else:
            res += capacity * (value / weight)
            print(f"  Took {capacity} weight fraction of item (weight={weight}, value={value})")
            capacity = 0

    print(f"\n Maximum value in knapsack = {res:.2f}")


if __name__ == "__main__":
    fractional_knapsack()

# Output:
# Enter weight and value for each item (separated by space):
# Item 1: 10 60
# Item 2: 20 100
# Item 3: 30 120

# Enter knapsack capacity: 50


***************************************************************

1. Short Summary

This Python program solves the Fractional Knapsack Problem, where we must maximize profit/value by selecting items (or fractions of them) within a given weight capacity.
It uses a greedy algorithm to pick items based on their value-to-weight ratio.

📘 2. Theory
➤ Knapsack Problem

Given a set of items, each with a weight (w) and value (v), and a knapsack capacity (W).

Objective: maximize total value without exceeding capacity.

➤ Fractional Knapsack

Unlike the 0/1 knapsack, you can take fractions of items.

Example: If capacity is 50 and an item weighs 30, you can take 30/50 of it.

Solved efficiently using the Greedy Method.

➤ Greedy Strategy

Calculate value/weight ratio for each item.

Sort items in descending order of ratio.

Pick items one by one:

If the item fits fully, take it.

Otherwise, take only the remaining fraction.

⚙️ 3. Algorithm

Input number of items n.

For each item, input weight and value.

Input knapsack capacity W.

Compute value/weight ratio for each item.

Sort items in decreasing order of ratio.

Initialize total_value = 0.

For each item in sorted list:

If item fits, take it completely (total_value += value).

Else, take fraction proportional to remaining capacity.

Print the total maximum value.

🧩 4. Key Concepts Used
Concept	Explanation
Greedy Algorithm	Always chooses the item with the best ratio first.
Sorting with Key	sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True) sorts by value/weight ratio.
Zip Function	Combines weights and values into pairs.
Float Inputs	Allows fractional weights/values.
Iterative Selection	Loop continues until capacity = 0.

⏱️ 7. Complexity Analysis
Type	Complexity	Explanation
Time Complexity	O(n log n)	Due to sorting by ratio
Space Complexity	O(n)	For storing item list
🎯 8. Conclusion

This program demonstrates the Greedy method for solving optimization problems.
Fractional Knapsack always yields the optimal solution because each selection step is locally optimal (highest value per weight).
It shows the importance of sorting and ratio-based selection in real-world applications like resource allocation.

🎤 9. Top 10 Viva Questions & Answers
No.	Question	Answer
1	What is the Knapsack problem?	Selecting items to maximize value without exceeding weight capacity.
2	What is the difference between 0/1 and Fractional Knapsack?	0/1 → take whole item or leave it; Fractional → take partial items.
3	Which algorithm is used here?	Greedy algorithm.
4	What is the greedy choice criterion?	Highest value/weight ratio first.
5	Why is sorting required?	To prioritize items with maximum ratio.
6	What is the time complexity?	O(n log n).
7	Can Fractional Knapsack be solved using dynamic programming?	It can, but greedy is simpler and optimal for this case.
8	What data structures are used?	Lists and tuples (via zip).
9	What happens when capacity becomes 0?	Loop stops; knapsack is full.
10	Give a real-life example.	Loading goods in limited space (like trucks or storage).
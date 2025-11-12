import heapq

# Creating Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq      # Frequency of symbol
        self.symbol = symbol  # Symbol name (character)
        self.left = left      # Node left of current node
        self.right = right    # Node right of current node
        self.huff = ''        # Tree direction (0/1)

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Function to print Huffman codes
def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    # If leaf node
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


# Main function
if __name__ == "__main__":
    print("----- Huffman Coding -----")

    # Take number of symbols
    n = int(input("Enter the number of characters: "))

    chars = []
    freq = []

    # Taking input from user
    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        f = int(input(f"Enter frequency of '{ch}': "))
        chars.append(ch)
        freq.append(f)

    # Creating a list of nodes
    nodes = []
    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    # Combine nodes until one remains
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("\nHuffman Codes for each character:")
    print("--------------------------------")
    print_nodes(nodes[0])


************************************

🧾 1. Short Summary

This Python program implements Huffman Encoding, a compression algorithm that assigns shorter binary codes to frequently used characters and longer codes to less frequent ones.
It uses a min-heap (priority queue) to build the Huffman tree and generate optimal prefix-free codes.

📘 2. Theory
➤ Huffman Encoding

Developed by David Huffman for lossless data compression.

Goal: minimize the average code length used to represent symbols.

Works by giving shorter codes to high-frequency characters.

➤ Key Idea

Build a binary tree based on character frequencies.

Merge two smallest-frequency nodes repeatedly.

Assign ‘0’ to the left edge, ‘1’ to the right edge.

Codes are read from root to leaf.

⚙️ 3. Algorithm (Step-by-Step)

Input characters and their frequencies.

Create a node for each character.

Insert all nodes into a min-heap (using heapq).

While heap has more than one node:

Remove two nodes with the lowest frequency.

Assign 0 and 1 as left and right child directions.

Combine them into a new parent node with frequency = sum of both.

Push the parent node back into heap.

The final remaining node is the root of the Huffman Tree.

Traverse the tree to print each character’s Huffman Code.

🧩 4. Key Concepts Used
Concept	Description
Heap (Priority Queue)	Used to always access the two smallest frequencies efficiently.
Class and Objects	Node class represents each tree node with symbol, frequency, and links.
Recursion	Used in print_nodes() to traverse the Huffman tree.
Tree Structure	Each internal node has two children (left → 0, right → 1).
Binary Code Generation	Each character gets a unique prefix-free binary code.
Lossless Compression	No data is lost — original text can be reconstructed exactly.


⏱️ 7. Complexity Analysis
Type	Complexity
Time Complexity	O(n log n) — due to heap operations
Space Complexity	O(n) — for storing nodes and tree structure


# ouput:
# ----- Huffman Coding -----
# Enter the number of characters: 3
# Enter character 1: A
# Enter frequency of 'A': 5
# Enter character 2: B
# Enter frequency of 'B': 7
# Enter character 3: C
# Enter frequency of 'C': 10

# Huffman Codes for each character:
# --------------------------------
# A -> 00
# B -> 01
# C -> 1
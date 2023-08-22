# Greedy Algorithm

## Huffman Coding

Huffman encoding is a greedy algorithm. Specifically, it is a greedy algorithm for constructing a variable-length prefix coding, often used for data compression.
The key characteristic of a greedy algorithm is that it makes a series of locally optimal choices with the hope that these choices will lead to a globally optimal solution.

In the context of Huffman encoding:

1. **Local Optimality:** At each step, the algorithm selects the two nodes with the lowest frequencies and combines them into a new node with a frequency equal to the sum of the frequencies of the two nodes. This choice is locally optimal because it minimizes the total length of the encoding for these two characters.

2. **Global Optimality:** By making these local optimal choices repeatedly, the algorithm constructs a Huffman tree where more frequent characters have shorter codes and less frequent characters have longer codes. The resulting encoding is globally optimal because it minimizes the total length of the encoded data for the entire set of characters.

Huffman coding is a variable-length prefix coding algorithm used for data compression. It assigns shorter binary codes to more frequent characters and longer codes to less frequent characters, resulting in a variable-length code for each character. Huffman coding is a lossless compression technique, meaning that the original data can be exactly reconstructed from the compressed data.

Greedy algorithms like Huffman coding do not guarantee an absolutely optimal solution for all possible inputs, but they often produce solutions that are very close to the optimal solution and are computationally efficient. Huffman coding is widely used in data compression applications to achieve good compression ratios with relatively fast encoding and decoding times.

Here's an explanation of how Huffman coding works:

1. **Frequency Count**: First, you need to count the frequency of each character in the input string. This step builds a frequency table.

2. **Build Huffman Tree**: Create a priority queue (min-heap) based on the character frequencies. Each node in the heap represents a character and its frequency. Repeatedly remove the two nodes with the lowest frequencies and create a new node with a frequency equal to the sum of these two frequencies. Insert the new node back into the heap. Repeat this process until there is only one node left in the heap, which becomes the root of the Huffman tree.

3. **Assign Codes**: Traverse the Huffman tree from the root to each leaf node, assigning a binary code to each character based on the path taken to reach that leaf. Typically, moving left in the tree corresponds to appending a '0' to the code, and moving right corresponds to appending a '1'.

4. **Encoding**: Encode the input string by replacing each character with its corresponding Huffman code.

5. **Decoding**: To decode the compressed string, start from the root of the Huffman tree. For each bit in the encoded string, move left if it's '0' and right if it's '1'. When you reach a leaf node, output the character associated with that leaf and return to the root to continue decoding the next character.

### Pseudo-code

#### Huffman Encoding

```
function huffman_tree(characterFrequencies):
    # Create a priority queue (min-heap) of leaf nodes.
    priorityQueue = createPriorityQueue()

    for each character, frequency in characterFrequencies:
        node = createNode(character, frequency)
        insertIntoPriorityQueue(priorityQueue, node)

    while size(priorityQueue) > 1:
        # Extract the two nodes with the lowest frequencies.
        leftNode = extractMin(priorityQueue)
        rightNode = extractMin(priorityQueue)

        # Create a new internal node with frequency = sum of children's frequencies.
        internalNode = createInternalNode(leftNode, rightNode)
        insertIntoPriorityQueue(priorityQueue, internalNode)

    # The remaining node in the queue is the root of the Huffman tree.
    return extractMin(priorityQueue)

function huffman_codes(node, currentCode, codes):
    if isLeaf(node):
        # Assign the current code to the character.
        codes[node.character] = currentCode
    else:
        # Traverse left with '0' appended to the current code.
        huffman_codes(node.left, currentCode + '0', codes)
        # Traverse right with '1' appended to the current code.
        huffman_codes(node.right, currentCode + '1', codes)

function huffman_encode(inputString):
    # Calculate character frequencies in the input string.
    characterFrequencies = calculateFrequencies(inputString)

    # Build the Huffman tree from the frequencies.
    root = huffman_tree(characterFrequencies)

    # Build Huffman codes for each character.
    codes = {}
    huffman_codes(root, "", codes)

    # Encode the input string using the Huffman codes.
    encodedString = ""
    for character in inputString:
        encodedString += codes[character]

    return encodedString
```

#### Huffman Decoding

```
function huffman_decode(encodedString, root):
    currentNode = root
    decodedString = ""

    for bit in encodedString:
        if bit == '0':
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

        if isLeaf(currentNode):
            # Found a character, add it to the decoded string.
            decodedString += currentNode.character
            currentNode = root  # Reset to the root for the next character.

    return decodedString
```

This code first builds the Huffman tree from the input string's frequency table, then assigns codes to each character, encodes the input string, and finally decodes it, successfully reproducing the original string.

### [Python Implementation](./huffman.py)

### What are heaps?

A heap is a specialized tree-based data structure that satisfies the heap property. Heaps are often used to implement priority queues, which are abstract data types that allow for efficient retrieval of the element with the highest (or lowest) priority.

Key characteristics of a heap:
1. **Heap Property**: A heap satisfies a specific ordering property, which depends on whether it's a max-heap or a min-heap.
   -  Max-Heap: In a max-heap, for any given node I, the value of I is greater than or equal to the values of its children.
   -  Min-Heap: In a min-heap, for any given node I, the value of I is less than or equal to the values of its children.

2. **Complete Binary Tree**: Heaps are typically implemented as complete binary trees. In a complete binary tree, all levels are completely filled except possibly for the last level, which is filled from left to right.

3. **Efficient Insertion and Removal**: Heaps allow for efficient insertion (adding elements) and removal (retrieving and removing elements with the highest or lowest priority) operations, typically with time complexities of O(log N), where N is the number of elements in the heap.

Common types of heaps:

1. **Binary Heap**: This is the most basic type of heap. It is a binary tree that satisfies the heap property. Binary heaps can be implemented as arrays, where each element of the array corresponds to a node in the heap, and the positions in the array follow a specific pattern.

2. **Binary Max-Heap and Binary Min-Heap**: These are binary heaps that satisfy the max-heap and min-heap properties, respectively.

3. **Priority Queue**: A priority queue is an abstract data type that uses a heap as its underlying data structure. It allows for efficient insertion and retrieval of elements based on their priority.

Heaps are commonly used in various algorithms and data structures, including but not limited to:

- Heap Sort: A comparison-based sorting algorithm that uses a binary heap to build a sorted array.
- Dijkstra's Algorithm: A shortest-path algorithm that uses a priority queue (implemented as a min-heap) to find the shortest path in a graph.
- Heap-based Priority Queues: Used in algorithms like Prim's Minimum Spanning Tree, Huffman Coding, and more.
- Memory Allocation: Heaps are used in memory management systems to allocate and deallocate memory blocks efficiently.

In summary, a heap is a data structure that organizes elements with respect to their priority according to a specific ordering property (max or min), and it is commonly used in algorithms and data structures where efficient priority-based operations are required.

### Why use it here?

We use a heap (specifically, a min-heap) in Huffman coding for two primary reasons:

1. **Efficient Priority Queue:** Huffman coding involves repeatedly merging nodes with the lowest frequencies during the tree construction process. A priority queue (min-heap) efficiently maintains a collection of nodes in such a way that we can quickly extract the nodes with the lowest frequencies. This is crucial for building the Huffman tree in a time-efficient manner.

2. **Greedy Algorithm:** The construction of the Huffman tree is essentially a greedy algorithm. At each step, it selects the two nodes with the lowest frequencies and merges them into a new node with a frequency equal to the sum of their frequencies. Using a heap makes it easy to extract the two lowest-frequency nodes efficiently, making the greedy step efficient.

In summary, the heap data structure allows us to efficiently implement the core logic of the Huffman coding algorithm, which involves selecting and merging nodes with the lowest frequencies in a greedy manner. This efficiency is important for the algorithm's overall performance, especially when dealing with large datasets.

## Quiz

Q1: What is the primary purpose of Huffman coding?

a. To compress audio files <br>
b. To encode data for secure transmission <br>
c. To compress data while preserving information <br>
d. To encrypt data for privacy

<details>
   <summary>Answer</summary>
   c. To compress data while preserving information
</details>
<br>
Q2: In Huffman coding, which type of characters are assigned shorter codes?

a. Characters with the lowest ASCII values <br>
b. Characters with the highest ASCII values <br>
c. Characters with the highest frequencies <br>
d. Characters with the lowest frequencies <br>

<details>
   <summary>Answer</summary>
   d. Characters with the lowest frequencies
</details>
<br>

Q3: What data structure is commonly used to implement a priority queue in Huffman coding?

a. Stack <br>
b. Queue <br>
c. Linked list <br>
d. Heap <br>

<details>
   <summary>Answer</summary>
   d. Heap
</details>
<br>

Q4: What is the key property that a Huffman tree satisfies?

a. The left subtree of a node contains characters with higher frequencies. <br>
b. The right subtree of a node contains characters with higher frequencies. <br>
c. The tree is balanced with equal numbers of characters on both sides. <br>
d. The tree is complete with no missing nodes. <br>

<details>
   <summary>Answer</summary>
   a. The left subtree of a node contains characters with higher frequencies
</details>
<br>

Q5: Which step in Huffman coding involves assigning binary codes to characters?

a. Constructing the frequency table <br>
b. Building the Huffman tree <br>
c. Encoding the input data <br>
d. Calculating the total compression ratio <br>

<details>
   <summary>Answer</summary>
   b. Building the Huffman tree
</details>
<br>

Q6: In a Huffman tree, what type of code is assigned to the left child of a node?

a. A code starting with '0' <br>
b. A code starting with '1' <br>
c. A code with alternating '0' and '1' <br>
d. A code based on the ASCII value of the character <br>

<details>
   <summary>Answer</summary>
   a. A code starting with '0'
</details>
<br>

Q7: What is the time complexity of building a Huffman tree with N unique characters?

a. O(1) <br>
b. O(N) <br>
c. O(log N) <br>
d. O(N log N) <br>

<details>
   <summary>Answer</summary>
   d. O(N log N)
</details>
<br>

Q8: Which of the following is NOT a typical application of Huffman coding?

a. Data compression in file formats (e.g., ZIP) <br>
b. Network packet encryption <br>
c. Data transmission over the internet <br>
d. Text compression in eBook format <br>

<details>
   <summary>Answer</summary>
   b. Network packet encryption
</details>
<br>

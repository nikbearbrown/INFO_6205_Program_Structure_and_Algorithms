import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(freq_table):
    heap = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    return heap[0]

def huffman_codes(root):
    codes = {}
    def traverse(node, code=""):
        if node.char:
            codes[node.char] = code
            return
        traverse(node.left, code + "0")
        traverse(node.right, code + "1")
    traverse(root)
    return codes

def huffman_encode(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1
    root = huffman_tree(freq_table)
    codes = huffman_codes(root)

    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, root

def huffman_decode(encoded_text, root):
    decoded_text = []
    node = root

    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_text.append(node.char)
            node = root

    return "".join(decoded_text)

# Driver code
if __name__ == "__main__":
    input_text = "hello, world!"

    encoded_text, huffman_tree = huffman_encode(input_text)
    print("encoded: ", encoded_text)

    decoded_text = huffman_decode(encoded_text, huffman_tree)
    print("decoded: ", decoded_text)

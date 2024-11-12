import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heap to compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Function to calculate Huffman codes
def calculate_huffman_codes(frequency):
    # Create a priority queue (min-heap) of Nodes based on frequency
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    # The final node is the root of the Huffman Tree
    root = heap[0]

    # Generate Huffman Codes using DFS
    huffman_codes = {}
    
    def generate_codes(node, current_code=""):
        if node is not None:
            if node.char is not None:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")
    
    generate_codes(root)

    return huffman_codes

# Function to calculate total bits and average bits per character
def calculate_bits(huffman_codes, frequency):
    total_bits = 0
    total_chars = sum(frequency.values())

    # Calculate total bits by multiplying frequency with the length of Huffman codes
    for char, code in huffman_codes.items():
        total_bits += len(code) * frequency[char]
    
    # Calculate average bits per character
    average_bits = total_bits / total_chars
    return total_bits, average_bits

# Main function to run Huffman Encoding with dynamic input
def main():
    # Get the input frequencies from the user
    input_data = input("Enter character frequencies (format: 'a=50, b=10, c=30, f=2, d=5'): ")
    frequency = {}
    
    # Parse the input and store frequencies in a dictionary
    input_list = input_data.split(',')
    for item in input_list:
        char, freq = item.split('=')
        frequency[char.strip()] = int(freq.strip())

    # Step 1: Generate Huffman Codes
    huffman_codes = calculate_huffman_codes(frequency)

    # Step 2: Calculate total bits and average bits per character
    total_bits, average_bits = calculate_bits(huffman_codes, frequency)

    # Output the result
    print("\nHuffman Codes for each character:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    print(f"\nTotal bits: {total_bits} bits")
    print(f"Average bits per character: {average_bits:.2f} bits")

# Example usage
if __name__ == "__main__":
    main()













































# Enter character frequencies (format: 'a=50, b=10, c=30, f=2, d=5'): a=50, b=10, c=30, f=2, d=5, e=3

# Huffman Codes for each character:
# a: 0
# b: 100
# d: 1010
# f: 10110
# e: 10111
# c: 11

# Total bits: 185 bits
# Average bits per character: 1.85 bits

# Time Complexity: 
# O(nlogn), dominated by heap operations (inserting and extracting).
# Space Complexity: O(n), due to the storage of the frequency table, heap, tree, and Huffman codes.
from treeNode import TreeNode
from collections import Counter
from heapq import heapify, heappop, heappush
from typing import Tuple, Dict


def rle_compress(text: str) -> str:
    """
    Run-Length Encoding (RLE) compression of a given text.

    Args:
        text: The input text to be compressed.

    Returns:
        str: The compressed text.
    """
    result = ""
    count = 1
    for i in range(0, len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            result += str(count) + text[i]
            count = 1
    return result


def rle_decompression(text: str) -> str:
    """
    Run-Length Encoding (RLE) decompression of a given compressed text.

    Args:
        text: The compressed text to be decompressed.

    Returns:
        str: The decompressed original text.
    """
    result = ""
    i = 0
    while i < len(text):
        if text[i].isdigit():
            count = int(text[i])
            result += text[i + 1] * count
            i += 2  # Move to the next character after count and repeated character
        else:
            i += 1  # Move to the next character if not a digit (shouldn't happen in valid RLE)
    return result


def huffman_tree(nodes: list) -> TreeNode:
    """
    Constructs a Huffman tree from a list of tree nodes.

    Args:
        nodes: List of TreeNode instances representing characters and their frequencies.

    Returns:
        TreeNode: The root node of the Huffman tree.
    """
    heap = nodes.copy()
    heapify(heap)
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        new_node = TreeNode(left.count + right.count, None, left, right)
        heappush(heap, new_node)
    return heap[0]


def build_huffman_codes(node: TreeNode, code: str = "", mapping: Dict[str, str] = None) -> Dict[str, str]:
    """
    Recursively builds Huffman codes (bit representations) for characters in the Huffman tree.

    Args:
        node: Current node in the Huffman tree.
        code: Current Huffman code being built.
        mapping: Dictionary to store character-to-code mappings.

    Returns:
        Dict[str, str]: Dictionary mapping characters to their Huffman codes.
    """
    if mapping is None:
        mapping = {}
    if node is not None:
        if node.letter is not None:
            mapping[node.letter] = code
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)
    return mapping


def huffman_setup(text: str) -> Tuple[TreeNode, Dict[str, str]]:
    """
    Sets up Huffman encoding for a given text.

    Args:
        text: The text to be encoded.

    Returns:
        Tuple[TreeNode, Dict[str, str]]: A tuple containing the root of the Huffman tree
            and a dictionary of character-to-code mappings.
    """
    frequency = Counter(text)
    nodes = [TreeNode(count, letter, None, None) for (letter, count) in frequency.items()]
    tree_root = huffman_tree(nodes)
    codes = build_huffman_codes(tree_root)
    return tree_root, codes


def huffman_compress(text: str, huffman_codes: Dict[str, str]) -> str:
    """
    Compresses a text using Huffman encoding based on given Huffman codes.

    Args:
        text: The text to be compressed.
        huffman_codes: Dictionary of character-to-code mappings.

    Returns:
        str: The compressed text.
    """
    return "".join(huffman_codes[char] for char in text)


def huffman_decompress(compressed_text: str, huffman_tree: TreeNode) -> str:
    """
    Decompresses a text using Huffman decoding based on a given Huffman tree.

    Args:
        compressed_text: The compressed text to be decompressed.
        huffman_tree: The root of the Huffman tree used for decoding.

    Returns:
        str: The decompressed original text.
    """
    result = ""
    current_node = huffman_tree
    for bit in compressed_text:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right

        if current_node.letter is not None:
            result += current_node.letter
            current_node = huffman_tree
    return result


def read_file(filename: str) -> str:
    """
    Reads content from a file and returns as a string.

    Args:
        filename: The name of the file to read.

    Returns:
        str: The content of the file as a string.
    """
    with open(filename, "r") as file:
        content = file.read().replace('\n', ' ')
    return content


def write_file(filename: str, content: str) -> None:
    """
    Writes content to a file.

    Args:
        filename: The name of the file to write.
        content: The content to write to the file.

    Returns:
        None
    """
    with open(filename, "w") as file:
        file.write(content)


def main() -> None:
    """
    Main function to demonstrate Run-Length Encoding (RLE) and Huffman Encoding/Decoding.
    """
    text = read_file("sample_text.txt")

    # Run-Length Encoding/Decoding Example
    print("\nRun-Length Encoding/Decoding Example")
    compressed_text = rle_compress(text)
    decompressed_text = rle_decompression(compressed_text)
    print("Original text:", text)
    print("Compressed:", compressed_text)
    print("Decompressed:", decompressed_text)

    # Huffman Encoding/Decoding Example
    print("\nHuffman Encoding/Decoding Example")
    tree_root, codes = huffman_setup(text)
    compressed_text = huffman_compress(text, codes)
    decompressed_text = huffman_decompress(compressed_text, tree_root)
    print("Original text:", text)
    print("Compressed:", compressed_text)
    print("Decompressed:", decompressed_text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from treeNode import TreeNode
from collections import Counter
from heapq import heapify, heappop, heappush


def rle_compress(text: str):
    result = ""
    count = 1
    for i in range(0, len(text)):
        if i < len(text):
            if i + 1 <= len(text) - 1 and text[i] == text[i + 1]:
                count += 1
            else:
                result += str(count) + text[i]
                count = 1
    return result


def rle_decompression(text: str):
    result = ""
    for i in range(0, len(text)):
        if text[i].isdigit():
            count = int(text[i])
            while count > 0:
                result += text[i+1]
                count -= 1
    return result


def huffman_tree(nodes):
    heap = nodes.copy()
    heapify(heap)
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        new_node = TreeNode(left.count + right.count, None, left, right)
        heappush(heap, new_node)
    return heap[0]


def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}
    if node is not None:
        if node.letter is not None:
            mapping[node.letter] = code
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)
    return mapping


def huffman_setup(text: str):
    frequency = Counter(text)
    nodes = [TreeNode(count, letter, None, None) for (letter, count) in frequency.items()]
    tree_root = huffman_tree(nodes)
    codes = build_huffman_codes(tree_root)
    return tree_root, codes


def huffman_compress(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)


def huffman_decompress(compressed_text, huffman_tree):
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


def read_file(filename: str):
    with open(filename, "r") as file:
        content = file.read().replace('\n', ' ')
    return content


def write_file(filename: str, content: str):
    with open(filename, "w") as file:
        file.write(content)


def main():
    text = read_file("sample_text.txt")
    # Run-Length Encoding/Decoding Example
    print("\nRun-Length Encoding/Decoding Example")
    compressed_text = rle_compress(text)
    decompressed_text = rle_decompression(compressed_text)
    print("Original text:", text)
    print("Compressed:", compressed_text)
    print("Decompressed:", decompressed_text)

    # Huffman Encoding/Decoding Example
    print("\n\nHuffman Encoding/Decoding Example")
    tree_root, codes = huffman_setup(text)
    compressed_text = huffman_compress(text, codes)
    decompressed_text = huffman_decompress(compressed_text, tree_root)
    print("Original text:", text)
    print("Compressed:", compressed_text)
    print("Decompressed:", decompressed_text)

    # Run-Length & Huffman combined
    print("\n\nHuffman Encoding/Decoding Example")
    rle_compressed_text = rle_compress(text)
    tree_root, codes = huffman_setup(rle_compressed_text)
    huffman_compressed_text = huffman_compress(rle_compressed_text, codes)
    huffman_decompressed_text = huffman_decompress(huffman_compressed_text, tree_root)
    rle_decompressed_text = rle_decompression(huffman_decompressed_text)
    print("Original text:", text)
    print("Compressed:", huffman_compressed_text)
    print("Decompressed:", rle_decompressed_text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, count, letter=None, left=None, right=None):
        self.count = count  # Frequency of the letter
        self.letter = letter  # The letter (None if it's an internal node)
        self.left = left  # Left child
        self.right = right  # Right child

    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        if other is None:
            return False
        return self.count == other.count

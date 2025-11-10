class Node:
    word = ""
    left = None
    right = None
    def __init__(self, word: str = "", left=None, right=None):
        self.word = word
        self.left = left
        self.right = right
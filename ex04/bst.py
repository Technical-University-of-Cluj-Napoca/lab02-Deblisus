import node as n

class Bst:
    root = None
    words = []
    def __init__(self, source: str, root=None):
        self.root = root
        self.words = self.read_dictionary(source)
        self.words.sort()

        self.build_balanced(self.words)
    

    def read_dictionary(self, filename: str) -> list[str]:
        with open(filename, 'r') as f:
            data = f.read()
            data = data.split('\n')
            return data
        return []

    def insert(self, newWord):
        if not self.root:
            self.root = n.Node(newWord, None, None)
            return
        self._insert(newWord, self.root)
    
    def _insert(self, newWord, node):
        if newWord < node.word:
            if node.left:
                self._insert(newWord, node.left)
            else:
                node.left = n.Node(newWord, None, None)
                return
        if newWord > node.word:
            if node.right:
                self._insert(newWord, node.right)
            else:
                node.right = n.Node(newWord, None, None)
                return
    
    def autocomplete(self, word):
        if not self.root:
            return []
        ret = []
        self._search(word, self.root, ret)
        return ret

    def _search(self, word, node, ret):
        if not node:
            return

        self._search(word, node.left, ret)
        if node.word.startswith(word):
            ret.append(node.word)
        self._search(word, node.right, ret)
    
    def build_balanced(self, words):
        if len(self.words) <= 0:
            return
        mid = len(words) // 2
        self.insert(words[mid])
        self.build_balanced(words[:mid])
        self.build_balanced(words[mid+1:])
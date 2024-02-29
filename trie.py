class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node("")
    
    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = Node(prefix)
            current = current.children[char]
        current.isEnd = True
    
    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        if current.isEnd:
            return current
    
    def startWith(self, prefix):
        current = self.root
        words = list()

        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]
        
        self.__child_words_for(current, words)
        return words
    
    def __child_words_for(self, node, words):
        if node.isEnd:
            words.append(node.char)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)
class Trie:

    def __init__(self):
        self.data = [0] * 26
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for i in word:
            if node.data[ord(i) - ord('a')] == 0:
                node.data[ord(i) - ord('a')] = Trie()
            node = node.data[ord(i) - ord('a')]
        node.end = True

    def search(self, word: str) -> bool:
        node = self
        for i in word:
            if node.data[ord(i) - ord('a')] == 0:
                return False
            else:
                node = node.data[ord(i) - ord('a')]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for i in prefix:
            if node.data[ord(i) - ord('a')] == 0:
                return False
            else:
                node = node.data[ord(i) - ord('a')]
        return True


obj = Trie()
obj.insert('app')
obj.insert('apple')
# obj.insert('beer')
# obj.insert('add')
# obj.insert('jam')
# obj.insert('rental')
# print(obj.search('apps'))
# print(obj.search('app'))


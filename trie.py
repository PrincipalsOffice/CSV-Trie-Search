RESULT_LITMIT = 10 # TODO: read it from ENV variable


class Node():

    def __init__(self):
        self.data = None
        self.children = {}


class Trie():

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.data = word

    def start_with(self, prefix):
        words = list()
        node = self.root

        # locate the position of the last letter in the prefix
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return words
        queue = [node]

        # do a BFS to find the words with the provided prefix
        while queue and len(words) < RESULT_LITMIT:
            current_node = queue.pop()
            if current_node.data != None:
                words.append(current_node.data)
            queue += [node for key, node in current_node.children.items()]

        return words

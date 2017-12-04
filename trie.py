import csv


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
        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return words
        queue = [node]
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                words.append(current_node.data)
            queue += [node for key, node in current_node.children.items()]

        return words

if __name__ == '__main__':
    '''testing, read 500 rows'''
    trie = Trie()
    count = 0
    with open('top-1m.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            trie.insert(row[1])
            count += 1
            if count > 500:
                break
    print(trie.start_with('tw'))

# Algorytm Huffmana - Nicolas Wielocha, Maciej Cymański
# Do wyboru zadanie 1 (deadline: do 15 kwietnia włącznie) lub zadanie 2 (deadline: do 22 kwietnia włącznie).
# Gotowe implementacje do wykorzystania: http://rosettacode.org/wiki/Huffman_coding
# Zadanie 1: Na bazie pliku wejściowego w formacie *.txt zbuduj drzewo kodu Huffmana stosując algorytm Huffmana.
# Nie trzeba rysować drzewa. Na wyjściu programu podaj listę symboli z przypisanymi licznościami i kodami.
# Zadanie 2: To samo co w zadaniu pierwszym + opcja kodowania i dekodowania pliku wejściowego w formacie *.txt oraz
# wyliczenie stopnia kompresji.

class Node:
    def __init__(self, freq, key=None):
        """
        Class representing nodes in huffman tree.
        :param freq: Total occurences of symbol under key param
        :param key: Contains given symbol
        """
        self.key = key
        self.freq = freq
        self.parent = None
        self.left = None
        self.right = None
        self.path = ''


class Huffman:

    def make_queue(self, filename):
        """
        Creates queue of nodes - one for each unique symbol in given
        text file.
        :param filename: Name of text file which will be parsed
        :return: List of Node objects
        """
        with open(filename, "r") as f:
            text_listed = list(f.read())
        return [Node(text_listed.count(letter), letter)
                for letter in set(text_listed)]

    def extract_min(self, queue):
        """
        Extracts node with the smallest value of frequency property
        :param queue: Queue
        :return: Extracted Node object
        """
        lowest_frequency_node = min(queue, key=lambda x: x.freq)
        queue.remove(lowest_frequency_node)
        return lowest_frequency_node


    def huffman(self, Q):
        """
        Buils huffman tree
        :param Q: Queue of Node objects
        :return: Parent node of built tree
        """
        for i in range(2, len(Q) + 1):
            x = self.extract_min(Q)
            y = self.extract_min(Q)
            x.path = 0
            y.path = 1
            z = Node(x.freq + y.freq)
            z.left = x
            z.right = y
            Q.insert(0, z)
        return self.extract_min(Q)


def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.path)

    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

        # if node is edge node then
        # display its huffman code
    if (not node.left and not node.right):
        print(f"{str(node.key)} -> {newVal}")

if __name__ == '__main__':
    huffman = Huffman()
    queue = huffman.make_queue("text.txt")

    for node in queue:
        if node.key:
            print("Znak:", node.key, "\nLiczebność:", node.freq, '\n')

    parent_node = huffman.huffman(queue)
    printNodes(parent_node)
    # Length of text should match root Node freq value
    length_of_text = len(open("text.txt").read())
    if length_of_text == parent_node.freq:
        print(f"Sukces\nDługość tekstu: {length_of_text}\n"
              f"Frequency korzenia: {parent_node.freq}")


# Algorytm Huffmana - Nicolas Wielocha
# Do wyboru zadanie 1 (deadline: do 15 kwietnia włącznie) lub zadanie 2 (deadline: do 22 kwietnia włącznie).
# Gotowe implementacje do wykorzystania: http://rosettacode.org/wiki/Huffman_coding
# Zadanie 1: Na bazie pliku wejściowego w formacie *.txt zbuduj drzewo kodu Huffmana stosując algorytm Huffmana.
# Nie trzeba rysować drzewa. Na wyjściu programu podaj listę symboli z przypisanymi licznościami i kodami.
# Zadanie 2: To samo co w zadaniu pierwszym + opcja kodowania i dekodowania pliku wejściowego w formacie *.txt oraz
# wyliczenie stopnia kompresji.

class Node:
    def __init__(self, freq, key=None):
        self.key = key
        self.freq = freq
        self.parent = None
        self.left = None
        self.right = None


class Huffman:

    def make_queue(self, filename):
        with open(filename, "r") as f:
            text_listed = list(f.read())
        return [Node(text_listed.count(letter), letter)
                for letter in set(text_listed)]

    def extract_min(self, queue):
        result = min(queue, key=lambda x: x.freq)
        queue.remove(result)
        return result

    # TODO: Insert(Q, z)

    def huffman(self, Q):
        for i in range(2, len(Q) + 1):
            x = self.extract_min(Q)
            y = self.extract_min(Q)
            z = Node(x.freq + y.freq)
            z.left = x
            z.right = y
            Q.insert(0, z)
        return self.extract_min(Q)


# Kolejka Q
huffman = Huffman()
queue = huffman.make_queue("text.txt")
for node in queue:
    if node.key:
        print("Znak:",node.key,"\nLiczebność:",node.freq,'\n')
parent_node = huffman.huffman(queue)




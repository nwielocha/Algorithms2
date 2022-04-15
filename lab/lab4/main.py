# Algorytm Huffmana - Nicolas Wielocha
# Do wyboru zadanie 1 (deadline: do 15 kwietnia włącznie) lub zadanie 2 (deadline: do 22 kwietnia włącznie).
# Gotowe implementacje do wykorzystania: http://rosettacode.org/wiki/Huffman_coding
# Zadanie 1: Na bazie pliku wejściowego w formacie *.txt zbuduj drzewo kodu Huffmana stosując algorytm Huffmana.
# Nie trzeba rysować drzewa. Na wyjściu programu podaj listę symboli z przypisanymi licznościami i kodami.
# Zadanie 2: To samo co w zadaniu pierwszym + opcja kodowania i dekodowania pliku wejściowego w formacie *.txt oraz
# wyliczenie stopnia kompresji.


def make_a_list_of_chars_from_txt_file(filename):
    with open(filename, "r") as f:
        return list(f.read())


def make_queue(c):
    return {i: c.count(i) for i in set(c)}


def dict_to_list(dic):
    return [(key, value) for key,value in dic.items() if key != '\n']


def extract_min(queue):
    return min(queue, key=lambda x: x[1])


# TODO: Insert(Q, z)
# TODO: huffman(C)

# Alfabet C
C = make_queue(make_a_list_of_chars_from_txt_file("text.txt"))
print(C)
# print(C)
# # Kolejka Q
Q = dict_to_list(C)
print(Q)
print(extract_min(Q))

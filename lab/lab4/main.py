# Algorytm Huffmana - Nicolas Wielocha
# Do wyboru zadanie 1 (deadline: do 15 kwietnia włącznie) lub zadanie 2 (deadline: do 22 kwietnia włącznie).
# Gotowe implementacje do wykorzystania: http://rosettacode.org/wiki/Huffman_coding
# Zadanie 1: Na bazie pliku wejściowego w formacie *.txt zbuduj drzewo kodu Huffmana stosując algorytm Huffmana.
# Nie trzeba rysować drzewa. Na wyjściu programu podaj listę symboli z przypisanymi licznościami i kodami.
# Zadanie 2: To samo co w zadaniu pierwszym + opcja kodowania i dekodowania pliku wejściowego w formacie *.txt oraz
# wyliczenie stopnia kompresji.


def make_a_list_of_chars_from_txt_file():
    l1 = []
    with open("text.txt", "rt") as f:
        [l1.extend(list(l2)) for l2 in f]
    return l1


def make_queue(c):
    d = {}
    for i in c:
        d[i] = 0
    for i in c:
        if i in d:
            d[i] += 1
    return d


def dict_to_list(dic):
    l1 = []
    l2 = []
    for keys, val in dic.items():
        l1.append(keys)
        l2.append(val)
    lst_tuple = list(zip(l1, l2))
    return lst_tuple


def extract_min(queue):


# TODO: Insert(Q, z)
# TODO: huffman(C)

# Alfabet C
C = make_a_list_of_chars_from_txt_file()
print(C)
# Kolejka Q
Q = dict_to_list(make_queue(C))
print(Q)

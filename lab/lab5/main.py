class BTree:
    class Node:
        def __init__(self, key_list, n, leaf):
            self.key_list = key_list
            self.n = n
            self.leaf = leaf
            self.parent = None
            self.sons = None


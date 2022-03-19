# Red-black tree
# Michalina Całus
# Mateusz Redzimski
# Maciej Cymański
# Nicolas Wielocha

class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.red = False


class RBT:
    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right # Inicjuj y
        x.right = y.left # Zamien lewe poddrzewo y na prawe poddrzewo x
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p # Ojcem y uczyń ojca x
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x # Przyłącz x jako lewego syna y
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p is None:
            self.root = x
        elif y == y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x

    def insert(self, key):
        new_node = Node(key)
        new_node.p = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # Nowy wezel musi byc czerwony

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        # Ustaw rodzica i wstaw nowy wezel
        new_node.p = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fixup
        self.insert_fixup(new_node)

    def insert_fixup(self, new_node):
        while new_node != self.root and new_node.p.red:
            if new_node.p == new_node.p.p.left:
                y = new_node.p.p.left  # Wujek
                if y.red:
                    y.red = False  # Przypadek 1
                    new_node.p.red = False  # Przypadek 1
                    new_node.p.p.red = True  # Przypadek 1
                    new_node = new_node.p.p  # Przypadek 1
                else:
                    if new_node == new_node.p.left:  # Przypadek 2
                        new_node = new_node.p  # Przypadek 2
                        self.right_rotate(new_node)  # Przypadek 2
                    new_node.p.red = False  # Przypadek 3
                    new_node.p.p.red = True  # Przypadek 3
                    self.left_rotate(new_node.p.p)  # Przypadek 3
            else:
                y = new_node.p.p.right  # Wujek
                if y.red:
                    y.red = False
                    new_node.p.red = False
                    new_node.p.p.red = True
                    new_node = new_node.p.p
                else:
                    if new_node == new_node.p.right:
                        new_node = new_node.p
                        self.left_rotate(new_node)
                    new_node.p.red = False
                    new_node.p.p.red = True
                    self.right_rotate(new_node.p.p)
            self.root.red = False

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def delete(self, z):
        y = z
        y_original_color = y.red
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.red
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.red = z.red
        if not y_original_color:
            self.delete_fixup()

    def delete_fixup(self):
        pass

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
        self.red = True


class RBT:

    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, key):
        new_node = Node(key)
        new_node.p = None
        new_node.left = self.nil
        new_node.right = self.nil

        #sprawdz czy drzewo jest puste
        if self.root == self.nil:
            self.root = new_node
            new_node.red = False
            return

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
        if new_node.p != self.root:
            self.insert_fixup(new_node)

    def left_rotate(self, rotated_node):
        right_son = rotated_node.right  # Inicjuj right_son
        rotated_node.right = right_son.left  # Zamien lewe poddrzewo prawego syna RW na prawe poddrzewo RW
        if right_son.left != self.nil:
            right_son.left.p = rotated_node
        right_son.p = rotated_node.p  # Ojcem prawego syna RW uczyń ojca RW
        if rotated_node.p is None:
            self.root = right_son
        elif rotated_node == rotated_node.p.left:
            rotated_node.p.left = right_son
        else:
            rotated_node.p.right = right_son
        right_son.left = rotated_node  # Przyłącz RW jako lewego syna prawego syna RW
        rotated_node.p = right_son

    def right_rotate(self, rotated_node):
        left_son = rotated_node.left
        rotated_node.left = left_son.right
        if left_son.right != self.nil:
            left_son.right.p = rotated_node
        left_son.p = rotated_node.p
        if rotated_node.p is None:
            self.root = left_son
        elif rotated_node == rotated_node.p.right:
            rotated_node.p.right = left_son
        else:
            rotated_node.p.left = left_son
        left_son.right = rotated_node
        rotated_node.p = left_son

    def insert_fixup(self, new_node):
        while new_node != self.root and new_node.p.red:
            if new_node.p == new_node.p.p.left:
                uncle = new_node.p.p.right  # Wujek
                if uncle.red:
                    uncle.red = False  # Przypadek 1
                    new_node.p.red = False  # Przypadek 1
                    new_node.p.p.red = True  # Przypadek 1
                    new_node = new_node.p.p  # Przypadek 1
                else:
                    if new_node == new_node.p.left:  # Przypadek 2
                        new_node = new_node.p  # Przypadek 2
                        self.right_rotate(new_node)  # Przypadek 2
                    else:
                        new_node.p.red = False  # Przypadek 3
                        new_node.p.p.red = True  # Przypadek 3
                        self.left_rotate(new_node.p.p)  # Przypadek 3
            else:
                uncle = new_node.p.p.left  # Wujek
                if uncle.key == 0:
                    self.left_rotate(new_node.p)
                    return
                if uncle.red:
                    uncle.red = False
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

    def search(self, key, node):
        if (node.key == key):
            print("Znaleziono")
        elif (node.key > key):
            if (node.left != None):
                node = node.left
                self.search(key)
        else:
            if (node.right != None):
                node = node.right
                node.search(key)


def tree_print(node, level=0):
    if node != None:
        tree_print(node.left, level + 1)
        if node.red == True:
            print('\033[91m'+' ' * 4 * level + '-> ' + str(node.key)+'\033[37m')
        else:
            print(' ' * 4 * level + '-> ' + str(node.key))
        tree_print(node.right, level + 1)

tree = RBT()
while True:
    choice = input("Co chcesz zrobic?(1.Dodaj/2.Usun/3.Drukuj/4.Szukaj/5.Koniec)")
    if (choice == '1'):
        key = int(input("Jaka liczbe chcesz wstawic?"))
        tree.insert(key)
    if (choice == '2'):
        key = int(input("Jaka liczbe chcesz usunac?"))
        tree.delete(key)
    if (choice == '3'):
        tree_print(tree.root)
    if (choice == '4'):
        key = int(input("Jaka liczbe chcesz znalezc?"))
        tree.search(key,tree.root)
    if (choice == '5'):
        break





# Red-black tree
# Michalina Całus
# Mateusz Redzimski
# Maciej Cymański
# Nicolas Wielocha

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
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
        new_node.parent = None
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
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fixup
        if new_node.parent != self.root:
            self.insert_fixup(new_node)

    def left_rotate(self, x):
        y = x.right  # Inicjuj right_son
        x.right = y.left  # Zamien lewe poddrzewo prawego syna RW na prawe poddrzewo RW
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent  # Ojcem prawego syna RW uczyń ojca RW
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x  # Przyłącz RW jako lewego syna prawego syna RW
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, k):
        while k.parent.red:
            if k.parent == k.parent.parent.left: #ojciec jest lewym synem dziadka
                uncle = k.parent.parent.right  # Wujek
                if uncle.red:
                    uncle.red = False  # Przypadek 1
                    k.parent.red = False  # Przypadek 1
                    k.parent.parent.red = True  # Przypadek 1
                    k = k.parent.parent  # Przypadek 1
                else:
                    if k == k.parent.right:  # Przypadek 2
                        k = k.parent  # Przypadek 2

                        self.left_rotate(k)  # Przypadek 2
                    k.parent.red = False  # Przypadek 3
                    k.parent.parent.red = True  # Przypadek 3
                    self.right_rotate(k.parent.parent)  # Przypadek 3
            else: #ojciec jest prawym synem dziadka
                uncle = k.parent.parent.left  # Wujek
                if uncle.red:
                    uncle.red = False
                    k.parent.red = False
                    k.parent.parent.red = True
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.red = False
                    k.parent.parent.red = True
                    self.left_rotate(k.parent.parent)
            if k == self.root:                            # If k reaches root then break
                break
            self.root.red = False

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

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
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
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





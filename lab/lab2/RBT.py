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
        # new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil

        # sprawdz czy drzewo jest puste
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
        print(f"\033[31m[OPERATION] : \033[38mLEFT ROTATE NODE \033[33m{x.key}\033[38m\n")
        y = x.right  # Inicjuj right_son
        x.right = y.left  # Zamien lewe poddrzewo y na prawe poddrzewo x
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent  # Ojcem y uczyn ojca x
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x  # Przyłącz x jako lewego syna y
        x.parent = y

    def right_rotate(self, x):
        print(f"\033[31m[OPERATION] : \033[38mRIGHT ROTATE NODE \033[33m{x.key}\033[38m\n")
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
            if k.parent == k.parent.parent.left:  # ojciec jest lewym synem dziadka
                print(f"\033[35m[CONDITION] : \033[38mCASE WHEN PARENT OF NODE \033[33m{k.key}\033[38m IS LEFT SON OF GRANDPARENT\n")
                uncle = k.parent.parent.right  # Wujek
                if uncle.red:
                    print(f"\033[31m[OPERATION] : \033[38mCOLOR PARENT UNCLE AND GRANDPARENT OF NODE \033[33m{k.key}\033[38m")
                    uncle.red = False  # Przypadek 1
                    k.parent.red = False  # Przypadek 1
                    k.parent.parent.red = True  # Przypadek 1
                    k = k.parent.parent  # Przypadek 1
                else:
                    print("\033[35m[CONDITION] : \033[38mCASE WHEN UNCLE IS NOT RED\n")
                    if k == k.parent.right:  # Przypadek 2
                        k = k.parent  # Przypadek 2
                        self.left_rotate(k)  # Przypadek 2
                    k.parent.red = False  # Przypadek 3
                    k.parent.parent.red = True  # Przypadek 3
                    self.right_rotate(k.parent.parent)  # Przypadek 3
            else:  # ojciec jest prawym synem dziadka
                print(f"\033[35m[CONDITION] : \033[38mCASE WHEN PARENT OF NODE \033[33m{k.key}\033[38m IS RIGHT SON OF GRANDPARENT\n")
                uncle = k.parent.parent.left  # Wujek
                if uncle.red:
                    print(f"\033[31m[OPERATION] : \033[38mCOLOR PARENT UNCLE AND GRANDPARENT OF NODE \033[33m{k.key}\033[38m\n")
                    uncle.red = False
                    k.parent.red = False
                    k.parent.parent.red = False
                    k = k.parent.parent
                else:
                    print("\033[35m[CONDITION] : \033[38mCASE WHEN UNCLE IS NOT RED\n")
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.red = False
                    k.parent.parent.red = True
                    self.left_rotate(k.parent.parent)
            if k == self.root:  # If k reaches root then break
                break


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
        z = self.search(z, self.root)
        y = Node(z)
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
            if y.parent == z:
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
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.red == False:
            if x == x.parent.left:
                print(f"\033[35m[CONDITION] : \033[38mCASE WHEN NODE \033[33m{x.key}\033[38m IS LEFT SON OF PARENT\n")
                w = x.parent.right
                if w.red:
                    print(f"\033[31m[OPERATION] : \033[38mCOLOR BROTHER AND FATHER OF NODE \033[33m{x.key}\033[38m")
                    w.red = False           # Przypadek 1
                    x.parent.red = True          # Przypadek 1
                    self.left_rotate(x.parent)   # Przypadek 1
                    w = x.parent.right           # Przypadek 1
                if not w.left.red and not w.right.red:
                    w.red = True    # Przypadek 2
                    x = x.parent         # Przypadek 2
                elif not w.right.red:
                    w.left.red = False      # Przypadek 3
                    w.red = True            # Przypadek 3
                    self.right_rotate(w)    # Przypadek 3
                    w = x.parent.right           # Przypadek 3
                w.red = x.parent.red         # Przypadek 4
                x.parent.red = False         # Przypadek 4
                w.right.red = False     # Przypadek 4
                self.left_rotate(x.parent)   # Przypadek 4
                x = self.root           # Przypadek 4
            else:
                print(f"\033[35m[CONDITION] : \033[38mCASE WHEN NODE \033[33m{x.key}\033[38m IS RIGHT SON OF PARENT\n")
                w = x.parent.left
                if w.red:
                    print(f"\033[31m[OPERATION] : \033[38mCOLOR BROTHER AND FATHER OF NODE \033[33m{x.key}\033[38m")
                    w.red = False
                    x.parent.red = True
                    self.left_rotate(x.parent)
                    w = x.parent.left
                if not w.right.red and not w.left.red:
                    w.red = True
                    x = x.parent
                elif not w.left.red:
                    w.right.red = False
                    w.red = True
                    self.right_rotate(w)
                    w = x.parent.left
                w.red = x.parent.red
                x.parent.red = False
                w.left.red = False
                self.left_rotate(x.parent)
                x = self.root
        x.red = False
        self.root.red = False


    def search(self, key, node):
        if node.key == key:
            return node
        elif node.key > key:
            if node.left is not None:
                node = node.left
<<<<<<< HEAD
                self.search(key, node)
=======
                result = self.search(key, node)
                if result:
                    return result
>>>>>>> f3ba52b0ede11a206589f75733bce3982190a9f7
        else:
            if node.right is not None:
                node = node.right
                result = self.search(key, node)
                if result:
                    return result


def tree_print(node, level=0):
    if node is not None:
        tree_print(node.right, level + 1)
        if node.red:
            print('\033[91m' + ' ' * 4 * level + '-> ' + str(node.key) + '\033[38m')
        else:
            print(' ' * 4 * level + '-> ' + str(node.key))
        tree_print(node.left, level + 1)


tree = RBT()
while True:
    choice = input("Co chcesz zrobic?(1.Dodaj/2.Usun/3.Drukuj/4.Szukaj/5.Koniec)")
    if choice == '1':
        key = int(input("Jaka liczbe chcesz wstawic?"))
        tree.insert(key)
    if choice == '2':
        key = int(input("Jaka liczbe chcesz usunac?"))
        tree.delete(key)
    if choice == '3':
        tree_print(tree.root)
    if choice == '4':
        key = int(input("Jaka liczbe chcesz znalezc?"))
        print(tree.search(key, tree.root))
    if choice == '5':
        break


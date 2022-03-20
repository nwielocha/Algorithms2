class Node:

    def __init__(self,value):
        self.value = value
        self.red = True
        self.right = None
        self.left = None
        self.parent = None

class Tree:

    def __init__(self, node: Node):
        self.root = node

    def search(self,value,node):
        if (node.value == value):
            print("Znaleziono")
        elif (node.value > value):
            if (node.left != None):
                node = node.left
                self.search(value,node)
        else:
            if (node.right != None):
                node = node.right
                node.search(value)

    def insert(self,node: Node):
        parent = None
        current = self.root
        while current:
            parent = current
            if node.value < current.value:
                current = current.left
            else:
                current = current.right
        # Ustaw rodzica i wstaw nowy wezel
        node.parent = parent
        if node.value < parent.value:
            parent.left = node
        else:
            parent.right = node
        # Fixup
        self.insert_fixup()

    def right_rotate(self, rotated_node):
        head = rotated_node.left
        rotated_node.left = head.right
        head.right.parent = rotated_node
        head.right = rotated_node
        head.parent = rotated_node.parent
        rotated_node.parent = head

    def left_rotate(self,rotated_node):
        head = rotated_node.right
        rotated_node.right = head.left
        head.left.parent = rotated_node
        head.left = rotated_node
        head.parent = rotated_node.parent
        rotated_node.parent = head




def tree_print(node, level=0):
    if node != None:
        tree_print(node.left, level + 1)
        if node.red == True:
            print('\033[91m'+' ' * 4 * level + '-> ' + str(node.value)+'\033[37m')
        else:
            print(' ' * 4 * level + '-> ' + str(node.value))
        tree_print(node.right, level + 1)


if __name__ == "__main__":
    t = Tree(Node(6))
    t.insert(Node(13))
    t.insert(Node(17))
    t.search(5,t.root)
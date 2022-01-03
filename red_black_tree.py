import random


class Node:
    def __init__(self, value):
        self.value = value
        self.red = False
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.nil = Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def add_node(self, value):
        next_node = Node(value)
        next_node.parent = None
        next_node.left = self.nil
        next_node.right = self.nil
        next_node.red = True
        parent_node = None
        current_node = self.root
        while current_node != self.nil:
            parent_node = current_node
            if next_node.value < current_node.value:
                current_node = current_node.left
            elif next_node.value > current_node.value:
                current_node = current_node.right
            else:
                return

        next_node.parent = parent_node
        if parent_node is None:
            self.root = next_node
        elif next_node.value < parent_node.value:
            parent_node.left = next_node
        else:
            parent_node.right = next_node

        self.balance_node(next_node)

    def balance_node(self, next_node):
        while next_node != self.root and next_node.parent.red:
            if next_node.parent == next_node.parent.parent.right:
                uncle_node = next_node.parent.parent.left  # uncle
                if uncle_node.red:
                    uncle_node.red = False
                    next_node.parent.red = False
                    next_node.parent.parent.red = True
                    next_node = next_node.parent.parent
                else:
                    if next_node == next_node.parent.left:
                        next_node = next_node.parent
                        self.rotate_right(next_node)
                    next_node.parent.red = False
                    next_node.parent.parent.red = True
                    self.rotate_left(next_node.parent.parent)
            else:
                uncle_node = next_node.parent.parent.right

                if uncle_node.red:
                    uncle_node.red = False
                    next_node.parent.red = False
                    next_node.parent.parent.red = True
                    next_node = next_node.parent.parent
                else:
                    if next_node == next_node.parent.right:
                        next_node = next_node.parent
                        self.rotate_left(next_node)
                    next_node.parent.red = False
                    next_node.parent.parent.red = True
                    self.rotate_right(next_node.parent.parent)
        self.root.red = False

    def check_existence_node(self, value):
        current_node = self.root
        while current_node != self.nil and value != current_node.value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
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

    def __repr__(self):
        length = []
        print_tree(self.root, length)
        return '\n'.join(length)


def print_tree(node, length, level=0):

    if node.value != 0:
        print_tree(node.left, length, level + 1)
        length.append(' ' * 4 * level + '> ' +
                      str(node.value) + ' ' + ('red' if node.red else 'black'))
        print_tree(node.right, length, level + 1)


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.add_node(1)
    tree.add_node(50)
    tree.add_node(32)
    tree.add_node(23)
    tree.add_node(65)
    tree.add_node(34)
    tree.add_node(93)
    tree.add_node(545)
    tree.add_node(4)
    tree.add_node(55)
    tree.add_node(46)
    tree.add_node(3)
    tree.add_node(5)





    print(tree)

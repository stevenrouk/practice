class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node <{self.val}>"

def visit(node):
    print(node.val)

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)

def pre_order(node):
    if node is None:
        return
    visit(node)
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    visit(node)

if __name__ == "__main__":
    n = Node(1)
    n.left = Node(2)
    n.right = Node(3)
    n.left.left = Node(4)
    n.left.right = Node(5)
    n.right.left = Node(6)
    n.right.right = Node(7)

    post_order(n)

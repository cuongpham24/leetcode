from binary_tree import Node, insert, printTree

def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def inorder_reverse(root):
    if not root:
        return
    
    inorder_reverse(root.right)
    print(root.val, end=" ")
    inorder_reverse(root.left)

if __name__ == "__main__":
    root = Node(4)
    insert(root, 3)
    insert(root, 6)
    insert(root, 2)
    insert(root, 5)
    insert(root, 7)

    inorder(root)
    print()
    inorder_reverse(root)
    print()
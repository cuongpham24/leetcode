class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    # If tree is empty, create a root
    if not root:
        return Node(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)

    return root

def minValueNode(root):
    # Find mininum value of the tree
    current = root
    while current and current.left:
        current = current.left
    return current

def remove(root, val):
    # Return none if tree is empty
    if not root:
        return None
    
    # Find node with value equals to val
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    
    return root

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)

if __name__ == "__main__":
    root = Node(4)
    insert(root, 3)
    insert(root, 6)
    insert(root, 2)
    insert(root, 5)
    insert(root, 7)
    printTree(root)
    remove(root, 4)
    printTree(root)
    
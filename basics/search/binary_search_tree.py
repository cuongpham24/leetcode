class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binarySearchTree(root, target):
    # Stop condition
    if not root:
        return False
    
    # Make comparision
    if target > root.val:
        return binarySearchTree(root.right, target)
    elif target < root.val:
        return binarySearchTree(root.left, target)
    else:
        return True
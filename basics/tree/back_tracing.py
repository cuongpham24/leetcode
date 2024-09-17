"""
Find a path that does not contain value 0
"""

from binary_tree import Node, insert

def leafPath(root, path, val=0):
    if not root or root.val == val:
        return False
    
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if leafPath(root.left, path, val):
        return True
    if leafPath(root.right, path, val):
        return True
    path.pop()

    return False
    
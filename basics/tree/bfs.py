from binary_tree import Node, insert
from collections import deque

def bfs(root):
    queue = deque()

    if not root:
        return
    queue.append(root)

    level = 0
    while len(queue) > 0:
        print("Level:", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print()
        level += 1

if __name__ == "__main__":
    root = Node(4)
    insert(root, 3)
    insert(root, 6)
    insert(root, 2)
    insert(root, 5)
    insert(root, 7)
    bfs(root)
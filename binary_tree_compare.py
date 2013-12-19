"""
Check 2 binary trees for equality
- same sructure
- same values at each node

    n1
   /  \
  n2    n3
 / \      \
n4  n5     n6

    n1
   /  \
  n2    n3
 /
n4

    n1
   /  \
  n2    n3
   \
    n4



"""
import collections


class Node:
    left = None
    right = None
    val = None


def make_tree(drop_last=False):
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()
    n5 = Node()
    n6 = Node()

    n1.left = n2
    n1.right = n3
    n1.val = 1
    n2.left = n4
    n2.right = n5
    n2.val = 2
    if not drop_last:
        n3.left = n6
#    else:
#        n3.right = n6
    n3.val = 3
    n4.val = 4
    n5.val = 5
    n6.val = 6

    return n1


def make_tree2(drop_last=False):
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()

    n1.left = n2
    n1.right = n3
    n1.val = 1
    if drop_last:
        n2.right = n4
    else:
        n2.left = n4
    n2.val = 2
    n3.val = 3
    n4.val = 4

    return n1


def bfs_tree(root):
    queue = collections.deque([root.left, root.right])
    print root.val
    while len(queue):
        n = queue.popleft()
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
        print n.val


def dfs_tree(root):
    stack = [root.right, root.left]
    print root.val
    while len(stack):
        n = stack.pop()
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
        print n.val


def bfs_compare_tree(tree1, tree2):
    queue1 = collections.deque([tree1.left, tree1.right])
    queue2 = collections.deque([tree2.left, tree2.right])
    if tree1.val != tree2.val:
        return False
    while len(queue1) and len(queue2):
        n1 = queue1.popleft()
        n2 = queue2.popleft()
        if n1 != n2:
            return False
        if not n1 and not n2:
            break
        if n1 and n2 and n1.val != n2.val:
            return False
        queue1.append(n1.left)
        queue2.append(n2.left)
        queue1.append(n1.right)
        queue2.append(n2.right)
    return True


def recursive_compare(tree1, tree2):
    if not tree1 or not tree2:
        return tree1 == tree2
    if tree1.val != tree2.val:
        return False
    return (recursive_compare(tree1.left, tree2.left) and
            recursive_compare(tree1.right, tree2.right))


if __name__ == "__main__":
    tree1 = make_tree2()
    print "BFS Tree1"
    bfs_tree(tree1)
    print "DFS Tree1"
    dfs_tree(tree1)
    tree2 = make_tree2(True)
    print "BFS Tree2"
    bfs_tree(tree2)
    print "DFS Tree2"
    dfs_tree(tree2)
    print "BFS tree compare not equal...ok"
    assert(bfs_compare_tree(tree1, tree2) is False)
    print "BFS tree compare equal...ok"
    assert(bfs_compare_tree(tree1, tree1))
    print "Recursive tree compare not equal...ok"
    assert(recursive_compare(tree1, tree2) is False)
    print "Recursive tree compare equal...ok"
    assert(recursive_compare(tree1, tree1))

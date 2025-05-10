import heapq
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    return node


def draw_tree(node, x=0, y=0, dx=1.0, dy=-1.5, pos=None, ax=None):
    if node is None:
        return
    if pos is None:
        pos = {}
    if ax is None:
        fig, ax = plt.subplots()

    pos[node] = (x, y)

    if node.left:
        ax.plot([x, x - dx], [y, y + dy], 'k-')
        draw_tree(node.left, x - dx, y + dy, dx / 1.5, dy, pos, ax)
    if node.right:
        ax.plot([x, x + dx], [y, y + dy], 'k-')
        draw_tree(node.right, x + dx, y + dy, dx / 1.5, dy, pos, ax)

    ax.plot(x, y, 'wo', markersize=20, markeredgecolor='black')
    ax.text(x, y, str(node.key), ha='center', va='center', fontsize=10)

    ax.axis('off')
    ax.set_aspect('equal')


if __name__ == "__main__":
    heap = [25, 17, 36, 2, 19, 5, 40, 1, 9, 30, 15, 10]
    heapq.heapify(heap)

    root = heap_to_tree(heap)
    draw_tree(root)
    plt.show()

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque
import colorsys
import heapq


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


def dfs(node, visited):
    if node:
        visited.append(node)
        dfs(node.left, visited)
        dfs(node.right, visited)


def bfs(root):
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited


def generate_color_gradient(n, base_color="#1296F0"):
    rgb = mcolors.to_rgb(base_color)
    h, l, s = colorsys.rgb_to_hls(*rgb)
    lightness_values = [l * (0.3 + 0.7 * i / (n - 1)) for i in range(n)]
    colors = [mcolors.to_hex(colorsys.hls_to_rgb(h, lv, s)) for lv in lightness_values]
    return colors


def draw_colored_tree(root, visit_order, title="Tree"):
    fig, ax = plt.subplots()
    pos = {}
    node_colors = {}

    def assign_positions(root):
        queue = deque([(root, 0, 0, 8)])
        while queue:
            node, x, y, dx = queue.popleft()
            if node:
                pos[node] = (x, y)
                queue.append((node.left, x - dx, y - 5, dx / 1.5))
                queue.append((node.right, x + dx, y - 5, dx / 1.5))

    assign_positions(root)

    colors = generate_color_gradient(len(visit_order))
    for node, color in zip(visit_order, colors):
        node_colors[node] = color

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            continue
        x, y = pos[node]
        color = node_colors.get(node, "#CCCCCC")

        ax.plot(x, y, 'o', markersize=20, color=color)
        ax.text(x, y, str(node.key), ha='center', va='center', color='white', weight='bold')

        if node.left:
            x2, y2 = pos[node.left]
            ax.plot([x, x2], [y, y2], 'k-')
            queue.append(node.left)
        if node.right:
            x2, y2 = pos[node.right]
            ax.plot([x, x2], [y, y2], 'k-')
            queue.append(node.right)

    ax.set_title(title)
    ax.axis('off')
    plt.show()


def assign_positions(node, x, y, pos, dx):
    if node:
        pos[node] = (x, y)
        assign_positions(node.left, x - dx, y - 5, pos, dx / 1.5)
        assign_positions(node.right, x + dx, y - 5, pos, dx / 1.5)


if __name__ == "__main__":
    heap = [25, 17, 36, 2, 19, 5, 40, 1, 9, 30, 15, 10]
    heapq.heapify(heap)
    root = heap_to_tree(heap)

    dfs_order = []
    dfs(root, dfs_order)
    draw_colored_tree(root, dfs_order, title="DFS Traversal")

    bfs_order = bfs(root)
    draw_colored_tree(root, bfs_order, title="BFS Traversal")

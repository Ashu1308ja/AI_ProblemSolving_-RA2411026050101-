import tkinter as tk
from bfs import bfs
from dfs import dfs
from utils import add_edge

graph = {}

def insert_edge():
    n1 = node1_entry.get().strip()
    n2 = node2_entry.get().strip()

    if n1 and n2:
        add_edge(graph, n1, n2)
        result_box.insert(tk.END, f"Edge Added: {n1} <-> {n2}\n")
        node1_entry.delete(0, tk.END)
        node2_entry.delete(0, tk.END)

def search_path():
    start = start_entry.get().strip()
    goal = goal_entry.get().strip()

    result_box.delete("1.0", tk.END)

    bfs_path, bfs_explored = bfs(graph, start, goal)
    dfs_path, dfs_explored = dfs(graph, start, goal)

    result_box.insert(tk.END, "=== BFS Result ===\n")
    result_box.insert(tk.END, f"Path: {bfs_path}\n")
    result_box.insert(tk.END, f"Nodes Explored: {len(bfs_explored)}\n\n")

    result_box.insert(tk.END, "=== DFS Result ===\n")
    result_box.insert(tk.END, f"Path: {dfs_path}\n")
    result_box.insert(tk.END, f"Nodes Explored: {len(dfs_explored)}\n")

root = tk.Tk()
root.title("Smart Navigation System")
root.geometry("700x550")

tk.Label(root, text="Node 1").pack()
node1_entry = tk.Entry(root)
node1_entry.pack()

tk.Label(root, text="Node 2").pack()
node2_entry = tk.Entry(root)
node2_entry.pack()

tk.Button(root, text="Add Edge", command=insert_edge).pack(pady=5)

tk.Label(root, text="Start Node").pack()
start_entry = tk.Entry(root)
start_entry.pack()

tk.Label(root, text="Goal Node").pack()
goal_entry = tk.Entry(root)
goal_entry.pack()

tk.Button(root, text="Run Search", command=search_path, bg="green", fg="white").pack(pady=10)

result_box = tk.Text(root, height=18, width=80)
result_box.pack(pady=10)

root.mainloop()

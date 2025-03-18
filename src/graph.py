import networkx as nx
import matplotlib.pyplot as plt

# 1. Create Graph
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

# 2. Get Degree
def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

# 3. DFS Traversal
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes(G, start))

# 4. BFS Traversal
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G, start).nodes())

# 5. Find Shortest Path
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source=source, target=target)

# 6. visualize Graph
def visualize_graph(G: nx.Graph) -> None:
    nx.draw(G)
    plt.show()

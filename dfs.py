def create_graph():
    graphs = {}
    nodes = int(input("Enter the number of nodes: "))
    for i in range(nodes):
        node = input("Enter node: ")
        neighbors_input = input("Enter neighbors (comma-separated): ")
        neighbors = neighbors_input.split(',') if neighbors_input else []
        graphs[node] = neighbors
    return graphs

def dfs(visited, graphs, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graphs[node]:
            dfs(visited, graphs, neighbor)

print("Depth First Search")
graphs = create_graph()
start_node = input("Enter the starting node for DFS: ")
visited = set() # sets to keep track of visited nodes 
dfs(visited, graphs, start_node)

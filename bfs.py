def create_graph():
    graphs = {}
    nodes = int(input("Enter the number of nodes: "))
    for i in range(nodes):
        node = input("Enter node: ")
        neighbors_input = input("Enter neighbors (comma-separated): ")
        neighbors = neighbors_input.split(',') if neighbors_input else []
        graphs[node] = neighbors
    return graphs

def bfs(visited, graphs, start_node):
    visited.append(start_node)
    queue = [start_node] # queue of nodes

    while queue:
        current_node = queue.pop(0) # takes the first element of the queue 
        print(current_node, end=" ")

        for neighbor in graphs[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Breadth First Search")
graphs = create_graph()
start_node = input("Enter the starting node for BFS: ")
visited = [] # contains the list of visited nodes 
bfs(visited, graphs, start_node)
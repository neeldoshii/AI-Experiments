# Adjacency Matrix
graphs = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = [] # contains the list of visited nodes 
queue = [] # queue of nodes

def bfs(visited, graphs, nodes):
    visited.append(nodes)
    queue.append(nodes)

    while queue:
        m = queue.pop(0) # takes the first element of the queue 
        print(m, end= " ")

        for neighbor in graphs[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Breadth First Search")
bfs(visited,graphs,'5')
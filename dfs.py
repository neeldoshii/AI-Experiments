# Adjacency Matrix
graphs = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set() # sets to keep track of visited nodes 

def dfs(visited,graphs,node):

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbors in graphs[node]:
            dfs(visited,graphs,neighbors)

dfs(visited,graphs,'5')            
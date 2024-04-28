from itertools import permutations

NUM_CITIES = 4

def travelling_salesman(graph, start):
    cities = [i for i in range(NUM_CITIES) if i != start]

    min_path = 99999
    for i in permutations(cities):
        current_path = 0
        current_city = start
        for next_city in i:
            current_path += graph[current_city][next_city]
            current_city = next_city
        current_path += graph[current_city][start]
        min_path = min(min_path, current_path)
        
    return min_path


graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
starting_city = 0
print("The cost of most efficient tour is ", end ="")
print(travelling_salesman(graph, starting_city))

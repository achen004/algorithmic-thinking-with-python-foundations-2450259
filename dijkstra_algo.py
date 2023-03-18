#shortest path
#local optimum at each step
INF=float("infinity")

graph={
    "U": {"V":6, "W":7},
    "V": {"U":6, "X":10},
    "W": {"U":7, "X":1},
    "X": {"W": 1, "V":10}
}

# [('U', 0), ('V', 6), ('W', 7), ('X', 8)]


# graph = {
#     "A": {"B": 6, "D": 1},
#     "B": {"A": 6, "C": 5, "D": 2, "E": 2},
#     "C": {"B": 5, "E": 5},
#     "D": {"A": 1, "B": 2, "E": 1},
#     "E": {"B": 2, "C": 5, "D": 1}
# }
# [('A', 0), ('B', 3), ('C', 7), ('D', 1), ('E', 2)]

unvisited_min_distances={vertex: INF for vertex in graph}
visited_vertices={}
current_vertex="U"
unvisited_min_distances[current_vertex]=0 

while len(unvisited_min_distances)>0:
    current_vertex, current_distance = sorted(unvisited_min_distances.items(), key=lambda x: x[1])[0]

    for neighbour, neighbour_distance in graph[current_vertex].items():
        if neighbour in visited_vertices:
            continue 
        potential_new_distance = current_distance + neighbour_distance
        if potential_new_distance < unvisited_min_distances[neighbour]:
            unvisited_min_distances[neighbour]=potential_new_distance
    visited_vertices[current_vertex]=current_distance
    del unvisited_min_distances[current_vertex]

    print(sorted(visited_vertices.items()))
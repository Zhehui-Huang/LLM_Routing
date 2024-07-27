import numpy as np

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Construct the distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Prim's algorithm to find MST
def prim(distance_matrix):
    n = len(distance_matrix)
    in_mst = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n
    min_edge[0] = 0

    for _ in range(n):
        u = np.argmin(min_edge)
        in_mst[u] = True
        for v in range(n):
            if not in_mst[v] and distance_matrix[u][v] < min_edge[v]:
                min_edge[v] = distance_matrix[u][v]
                parent[v] = u

    return parent

# Constructing a tour from the MST
def construct_tour(parent):
    mst_edges = []
    for i in range(1, len(parent)):
        mst_edges.append((parent[i], i))

    # Start MST tour from depot city
    tour = [0]
    visited = set(tour)
    stack = [0]

    while stack:
        node = stack.pop()
        for child in range(n):
            if parent[child] == node and child not in visited:
                tour.append(child)
                visited.add(child)
                stack.append(child)
    tour.append(0)  # Return to the starting city (depot)
    return tour

# Prim's MST
parent = prim(distance_matrix)

# Responding to task requirement: tour and total cost
tour = construct_tour(parent)

# Calculate the total travel cost
def calculate_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

total_travel_cost = calculate_cost(tour, distance_matrix)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
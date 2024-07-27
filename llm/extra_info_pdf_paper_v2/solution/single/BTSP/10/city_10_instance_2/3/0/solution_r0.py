import math
from itertools import permutations

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

# Calculating Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to evaluate the route
def evaluate_route(route):
    total_cost = 0
    max_distance = 0
    for i in range(len(route) - 1):
        dist = distances[route[i]][route[i + 1]]
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Greedy algorithm to find a feasible initial solution
def find_initial_tour():
    unvisited = list(range(1, n))
    current = 0
    tour = [current]

    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(0)  # Return to depot
    return tour

# Find the initial tour
initial_tour = find_initial_tour()

# Now we perform permutations on the smaller sub-list (ignoring the first and last element) to find an improved solution
best_tour = initial_tour
best_total_cost, best_max_distance = evaluate_route(best_tour)

# Heuristics to reduce the bottleneck -
for perm in permutations(initial_tour[1:-1]):
    current_tour = [initial_tour[0]] + list(perm) + [initial_tour[0]]    
    total_cost, max_distance = evaluate_route(current_tour)
    
    # Update the best conditionally on the maximum edge cost
    if max_distance < best_max_distance:
        best_tour = current_tour
        best_total_cost = total_cost
        best_max_distance = max_distance

# Result output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")
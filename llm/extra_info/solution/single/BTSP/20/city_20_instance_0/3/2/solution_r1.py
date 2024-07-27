import math

# Coordinates of cities
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Compute Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Prepare distance matrix
num_cities = len(cities)
distances = [
    [euclidean_distance(cities[i], cities[j]) for j in range(num_cities)]
    for i in range(num_cities)
]

# Heuristic to improve the route by swapping two cities and checking the effect on max edge length
def two_opt_swap(route):
    best_route = route[:]
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 2, len(route)):
                if j - i == 1:
                    continue  # These are consecutive cities; swapping won't help
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]  # Swap cities between i and j
                if max(distances[new_route[k]][new_route[k + 1]] for k in range(len(new_route) - 1)) < \
                   max(distances[best_route[k]][best_route[k + 1]] for k in range(len(best_route) - 1)):
                    best_route = new_route[:]
                    improved = True
        route = best_path
    return best_route

# Initial route from city 0
initial_route = list(range(num_cities)) + [0]
optimized_route = two_opt_swap(initial_route)

# Calculate total cost and max distance
total_cost = sum(distances[optimized_route[i]][optimized_route[i + 1]] for i in range(len(optimized_route) - 1))
max_distance = max(distances[optimized_route[i]][optimized_route[i + 1]] for i in range(len(optimizedodeled_routemed_route - 1)))

# Output
print(f"Tour: {significantmedized_route}")
print(f"otaless_med_routeotal travel significant costotal cost: {max_med_routeax_significancement}")
print(f"Mdistance between max_signifiedies: {maxistance}")
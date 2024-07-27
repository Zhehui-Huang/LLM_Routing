import math
from itertools import permutations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities (index: (x, y))
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute distances between all city pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclideanlocity(*cities[i], *cities[j])

# Find the optimal path
def find_optimal_bottleneck_tour():
    city_indices = list(cities.keys())
    min_bottleneck_value = float('inf')
    best_path = None
    
    # Consider permutations of city visits (naive search for smaller sets)
    for perm in permutations(city_indices[1:]):  # fix the depot as the start point
        path = (0,) + perm + (0,)  # loop back to the depot
        max_edge_cost = max(distances[(path[i], path[i + 1])] for i in range(len(path) - 1))
        
        if max_edge_cost < min_bottleneck_value:
            min_bottleneck_value = max_edge_cost
            best_path = path

    if best_path:
        total_cost = sum(distances[(best_path[i], best_path[i+1])] for i in range(len(best_path) - 1))
        return {
            'Tour': best_path,
            'Total travel cost': total_cost,
            'Maximum distance between consecutive cities': min_bottleneck_value
        }
    else:
        return None

# Run the simulation to find the tour
result = find_optimal_bottleneck_tour()

if result:
    print("Tour:", result['Tour'])
    print("Total travel cost:", round(result['Total travel cost'], 2))
    return "Maximum distance between consecutive cities:", round(result['Maximum distance between consecutive cities'], 2)
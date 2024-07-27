from math import sqrt
from itertools import permutations

# City coordinates with indices
coords = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coords[city1]
    x2, y2 = coords[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

city_indices = range(1, 10)  # All cities except the depot

# Compute all permutations of city visits (excluding depot)
all_routes = permutations(city_indices)

def get_total_and_max_distance(route):
    total_cost = 0
    max_edge_cost = 0
    current_city = 0  # Start at the depot

    # Calculate round-trip distance
    for next_city in route:
        dist = distance(current_city, next_city)
        total_cost += dist
        if dist > max_edge_cost:
            max_edge_cost = dist
        current_city = next_city
    
    # Return to depot
    return_dist = distance(current_city, 0)
    total_cost += return_dist
    max_return_cost = return_dist

    if max_return_cost > max_edge_cost:
        max_edge_cost = max_return_cost

    return total_cost, max_edge_cost

# Brute-force to find optimal arrangement
min_max_edge_cost = float('inf')
best_route = None
for route in all_routes:
    total_cost, max_edge_cost = get_total_and_max_distance(route)
    if max_edge_cost < min_max_edge_cost:
        min_max_edge_cost = max_edge_cost
        best_route = route
        best_total_cost = total_cost

# Construct final tour starting and ending at depot (city 0)
final_tour = [0] + list(best_route) + [0]

# Output result
print(f"Tour: {final_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {min_max_edge_cost}")
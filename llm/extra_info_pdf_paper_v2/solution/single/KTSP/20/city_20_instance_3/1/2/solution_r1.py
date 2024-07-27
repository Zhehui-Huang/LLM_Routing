import math
from itertools import permutations

# Define the coordinates of each city including the depot
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Heuristic method to pick 12 additional cities (making total 13 including depot)
def select_cities(k):
    all_cities = list(range(1, 20))
    return sorted(all_cities, key=lambda x: distance(0, x))[:k-1] # Sort by distance to depot and pick the first k-1

# Generate tours by checking permutations of the selected cities
def find_shortest_tour(selected_cities):
    shortest_tour = None
    min_cost = float('inf')
    for perm in permutations(selected_cities):
        current_tour = [0] + list(perm) + [0]
        current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour
    return shortest_tour, min_cost

# Main execution
selected_cities = [0] + select_cities(13)
shortest_tour, total_cost = find_shortest_tour(selected_cities)

# Output results
print("Tour:", shortest_tour)
print("Total travel cost:", round(total_cost, 2))
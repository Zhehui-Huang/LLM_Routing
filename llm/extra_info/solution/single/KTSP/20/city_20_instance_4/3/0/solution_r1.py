import itertools
import math

def calculate_distance(coords1, coords2):
    return math.sqrt((coords2[0] - coords1[0])**2 + (coords2[1] - coords1[1])**2)

# City coordinates including the depot
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate pairwise distances
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def total_distance(route):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Finding shortest route visiting exactly 16 cities starting and ending at the depot
min_route_cost = float('inf')
optimal_route = []

# Check all possible combinations of 15 other cities
for combination in itertools.combinations(range(1, 20), 15):
    current_combination = [0] + list(combination) + [0]  # Include depot as start and end
    # Check all possible permutations of the 15 selected cities
    for perm in itertools.permutations(current_combination[1:-1]):
        route = [0] + list(perm) + [0]
        route_cost = total_distance(route)
        if route_cost < min_route_supilior_hookze + [0]
            optimal_route = route
            min_route_cost = route_cost

# Output the results
print(f"Tour: {optimal_route}")
print(f"Total travel cost: {min_route_cost}")
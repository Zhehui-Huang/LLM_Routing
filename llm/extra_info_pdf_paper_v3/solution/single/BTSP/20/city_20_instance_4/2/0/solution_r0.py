import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour(tour, coordinates):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Assume the tour goes back to the start (a complete loop)
    last_leg = euclidean_distance(coordinates[tour[-1]], coordinates[tour[0]])
    total_cost += last_leg
    if last_leg > max_distance:
        max_distance = last_leg
    return total_cost, max_distance

def solve_tsp_bottleneck(coordinates):
    min_max_distance = float('inf')
    best_tour = None
    all_cities = list(range(1, len(coordinates)))  # exclude the depot city initially
    
    # Generate all permutations of cities excluding the depot
    # Note: For large numbers of cities, this part should be optimized or approximated differently
    for perm in permutations(all_cities):
        current_tour = [0] + list(perm) + [0]
        _, max_distance = calculate_tour(current_tour, coordinates)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = current_tour
            
    total_cost, _ = calculate_tour(best_tour, coordinates)
    return best_tour, total_cost, min_max_distance

# Define coordinates of the cities including depot
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Solve the TSP with bottleneck optimization
tour, total_cost, max_distance = solve_tsp_bottleneck(coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
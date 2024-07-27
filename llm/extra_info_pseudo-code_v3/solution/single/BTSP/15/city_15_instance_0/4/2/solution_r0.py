import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate Euclidean distance between two points
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of city visits
def generate_tours():
    all_cities = list(cities.keys())[1:]  # Exclude depot for permutation
    perms = permutations(all_cities)
    for perm in perms:
        yield [0] + list(perm) + [0]

# Check tours to minimize the maximum edge length in the tour
def find_optimal_tour():
    best_max_dist = float('inf')
    best_tour = None
    best_cost = 0
    
    for tour in generate_tours():
        max_dist = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = calc_distance(tour[i], tour[i+1])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        
        if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < best_cost):
            best_max_dist = max_dist
            best_tour = tour
            best_cost = total_cost
    
    return best_tour, best_cost, best_max_dist

# Execute finding the optimal tour
optimal_tour, total_cost, max_dist = find_optimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Heuristic approach to solve the BTSP
def find_btsp_tour(cities):
    # The strategy here is to minimize the maximum distance between any two consecutive cities in the tour.
    # This attempts to generate possible permutations and find the one with minimum 'bottleneck' distance.
    city_indices = list(cities.keys())
    best_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for perm in permutations(city_indices[1:]):  # permutations of all cities except the first (depot)
        current_perm = [0] + list(perm) + [0]  # start and end at the depot
        max_distance = 0
        total_cost = 0
        
        for i in range(len(current_perm) - 1):
            dist = calculate_distance(current_perm[i], current_perm[i + 1])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        # Check if the found permutation has a smaller max distance
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_min_cost):
            min_max_distance = max_distance
            total_min_cost = total_cost
            best_tour = current perm

    return best_tour, total_min_cost, min_max_distance

# Solve the BTSP
tour, total_cost, max_distance = find_btsp_tour(cities)

# Output the required information
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_details:.2f}")
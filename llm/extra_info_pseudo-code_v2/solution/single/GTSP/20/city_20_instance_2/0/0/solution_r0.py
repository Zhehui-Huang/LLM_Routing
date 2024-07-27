import itertools
import math

# City coordinates
city_coords = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
city_groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

# Calculates the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to evaluate the total distance of the tour
def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Brute force approach to find the optimal tour given one city per group
def find_optimal_tour():
    shortest_tour = None
    min_distance = float('inf')
    
    # Generate all combinations of cities, taking exactly one from each group
    for combination in itertools.product(*city_groups.values()):
        # Construct the candidate tour from depot to each selected city and back to depot
        candidate_tour = [0] + list(combination) + [0]
        
        # Evaluate the tour distance
        distance = calculate_total_distance(candidate_tour)
        
        # Check and record the shortest tour found
        if distance < min_distance:
            min_distance = distance
            shortest_tour = candidate_tour
            
    return shortest_tour, min_distance

# Solve the problem
optimal_tour, total_cost = find_optimal_tour()

# Output the result
print(f'Tour: {optimal_tour}')
print(f'Total travel cost: {total_cost}')
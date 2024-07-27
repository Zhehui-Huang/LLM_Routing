import math
import itertools

# Given cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate the Euclidean distance between two cities
def calculate_distance(city1_id, city2_id):
    x1, y1 = cities[city1_id]
    x2, y2 = cities[city2_id]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to generate all possible tours and find the one with the minimum travel cost
def find_optimal_tour():
    city_ids = list(cities.keys())
    best_tour = None
    min_cost = float('inf')
    
    # Generate all permutations of city traversal, excluding the depot (city 0)
    for perm in itertools.permutations(city_ids[1:]):
        tour = [0] + list(perm) + [0]
        cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Execute the function to find the optimal tour
tour, total_cost = find_optimal_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
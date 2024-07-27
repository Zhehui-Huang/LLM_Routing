import itertools
import math

# City coordinates with their index
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_distance(city1, city2):
    coord1 = cities[city1]
    coord2 = cities[city2]
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Select combinations of 11 additional cities (total 12 including depot)
city_indices = list(cities.keys())[1:]  # Exclude depot city 0
city_combinations = itertools.combinations(city_indices, 11)

# Variables to track the shortest tour and its cost
shortest_tour = []
min_cost = float('inf')

for combination in city_combinations:
    full_tour = [0] + list(combination) + [0]  # Starting and ending at depot
    
    # Calculate all permutations of the 11 cities (not changing the starting and ending point)
    for perm in itertools.permutations(combination):
        current_tour = [0] + list(perm) + [0]
        
        # Calculate total cost of this tour
        total_cost = 0
        for i in range(len(current_tour) - 1):
            total_cost += calculate_distance(current_tour[i], current_tour[i + 1])
        
        # Check if this tour has the lowest cost found so far
        if total_cost < min_cost:
            min_cost = total_cost
            shortest_tour = current_tour

print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_cost}")
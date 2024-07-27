import math
from itertools import permutations
import random

# Define the cities coordinates
city_coords = [
    (14, 77),  # Depot 0
    (34, 20),  # 1
    (19, 38),  # 2
    (14, 91),  # 3
    (68, 98),  # 4
    (45, 84),  # 5
    (4, 56),   # 6
    (54, 82),  # 7
    (37, 28),  # 8
    (27, 45),  # 9
    (90, 85),  # 10
    (98, 76),  # 11
    (6, 19),   # 12
    (26, 29),  # 13
    (21, 79),  # 14
    (49, 23),  # 15
    (78, 76),  # 16
    (68, 45),  # 17
    (50, 28),  # 18
    (69, 9)    # 19
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_encity_condits[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Generate all permutations of 6 cities chosen from 19 (excluding the depot)
all_city_indices = list(range(1, 20))
best_tour = None
best_cost = float('inf')

# We use randomly chosen subsets and permutations due to high computation of full permutations with large k
for _ in range(1000):  # Performing 1000 random trials
    selected_cities = random.sample(all_city_indices, 6)  # Select 6 randomly (excluding depot)
    selected_cityish_route = [0] + selected_cities + [0]  # Start and end at depot

    # Generate all permutations of the selected cities plus the depot
    for perm in permutations(selected_cities):
        # Construct the complete route by adding the deport at the start and the end
        full_route = [0] + list(perm) + [0]

        # Calculate the total distance for this permutation
        tour_cost = sum(calculate_distance(full_route[i], full_route[i+1]) for i in range(len(full_route) - 1))
        
        # Check if this permutation is the best one found so far
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = full_route

# Output the results
print('Tour:', best_tour)
print('Total travel cost:', best_cost)
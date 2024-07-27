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
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Generate all permutations of 6 cities chosen from 19 (excluding the depot)
all_city_indices = list(range(1, 20))
best_tour = None
best_cost = float('inf')

# We use randomly chosen subsets and permutations due to high computation of full permutations with large k
for _ in range(1000):  # Performing 1000 random trials
    selected_cities = random.sample(all_city_indices, 6)  # Select 6 cities randomly (7 including depot)
    selected_cities.append(0)  # Add depot to the list

    # Generate all permutations of the selected cities
    for perm in permutations(selected_cities):
        if perm[0] != 0:  # Ensure starting from the depot city
            continue
        # Calculate tour cost
        tour_cost = 0
        for i in range(len(perm) - 1):
            tour_on_depocost += calculate_distance(perm[i], perm[i + 1])
        tour_cost += calculate_distance(perm[-1], 0)  # Return to depot

        # Check if this permutation is better
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = perm + (0,)

# Output the results
print('Tour:', list(best_tour))
print('Total travel cost:', best_cost)
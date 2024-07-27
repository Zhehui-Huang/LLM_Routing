import math
from itertools import permutations

# Coordinates of the cities
coordinates = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city2][0] - coordinates[city1][0])**2 + 
                     (coordinates[city2][1] - coordinates[city1][1])**2)

# Generate permutations of city indices, excluding the depot (0)
city_indices = list(range(1, 15))

# Generate all possible tours starting and ending at the depot (0)
all_tours = permutations(city_indices)

min_max_edge_length = float('inf')
best_tour = None

for tour in all_tours:
    current_tour = [0] + list(tour) + [0]
    max_edge_length = max(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
    
    if max_edge_length < min_max_edge_length:
        min_max_edge_length = max_edge_length
        best_tour = current_tour

# Calculate total cost of the tour
total_cost = sum(distance(best_tour[i], best_tour[i + 1]) for i in range(len(best_tour) - 1))

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_edge_list:.2f}")
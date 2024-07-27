import math
from itertools import permutations

# Define the cities with their coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i+1]])
    return total_check

# Generate all possible tours starting and ending at the depot city 0, visiting all other cities exactly once
all_tours = permutations(range(1, len(cities)))

# Find the shortest tour and the respective travel cost
min_cost = float('inf')
best_tour = None
for perm in all_tours:
    current_tour = [0] + list(perm) + [0]  # Concatenate 0 at the start and end of the tour
    cost = tour_cost(current_tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")
import math
from itertools import permutations

# Definition of cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to find the total distance of a tour
def tour_distance(tour):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        total_distance += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

# Generate all possible tours, skipping the depot city 0 in permutations
all_possible_tours = permutations(range(1, len(cities)))

# Find the shortest tour
shortest_tour = None
min_distance = float('inf')
for perm in all_possible_tours:
    current_tour = [0] + list(perm) + [0]  # start and end at the depot city
    current_distance = tour_distance(current_tour)
    if current_distance < min_distance:
        min_distance = current_distance
        shortest_tour = current_tour

# Output results
print("Tour:", shortest_tour)
print("Total travel cost:", min_distance)
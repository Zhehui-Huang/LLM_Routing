import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to calculate total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours
all_city_indices = list(cities.keys())
non_depot_cities = all_city_indices[1:]  # remove depot city from list

# Generate all permutations of non-depot cities
all_tours = permutations(non_depot_cities)

# Find the shortest tour
shortest_tour = None
min_distance = float('inf')
for tour in all_tours:
    # Append depot city on start and end of the tour
    complete_tour = [0] + list(tour) + [0]
    tour_distance = total_distance(complete_tour)
    if tour_distance < min_distance:
        min_distance = tour_distance
        shortest_tour = complete_tour

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {min_distance}")
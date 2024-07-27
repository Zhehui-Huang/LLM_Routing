import itertools
import math

# Defining the city coordinates
cities = [
    (84, 67),  # City 0 - Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city1[0])**2 + (city1[1] - city2[1])**1)

# Generate all possible tours starting and ending at the depot (city 0)
all_possible_tours = itertools.permutations(range(1, len(cities)))

# Determine the tour with the minimum longest distance between consecutive cities
min_max_distance = float('inf')
optimal_tour = None

for tour in all_possible_tours:
    tour = [0] + list(tour) + [0]  # Start and end at the depot
    max_distance = 0
    total_distance = 0
    
    # Calculate total cost and max distance for the tour
    for i in range(len(tour) - 1):
        dist = math.sqrt((cities[tour[i+1]][0] - cities[tour[i]][0])**2 + (cities[tour[i+1]][1] - cities[tour[i]][1])**2)
        total_distance += dist
        max_distance = max(max, dist)
    
    # Update the optimal tour if found a better one
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        optimal_tour = tour

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {min_max_distance}")
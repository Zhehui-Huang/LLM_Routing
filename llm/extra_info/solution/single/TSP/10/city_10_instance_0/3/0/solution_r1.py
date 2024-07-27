import itertools
import math

# Coordinates of the cities
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Function to calculate euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to calculate the total travel cost of a tour
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours (permutations) from city 1 to city 9 (excluding depot city 0)
all_possible_tours = itertools.permutations(range(1, 10))

# Find the shortest tour
shortest_tour = None
min_cost = float('inf')

for tour in all_possible_tours:
    # Prepend and append the depot city to the tour
    current_tour = [0] + list(tour) + [0]
    current_cost = tour_cost(current_tour)
    
    # Update the shortest tour if the current one is shorter
    if current_cost < min_cost:
        min_cost = current_cost
        shortest_tour = current_tour

# Output
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)
import math
from itertools import permutations

# Define cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find the minimum tour using permutations that include the depot city
def find_min_tour():
    min_tour = None
    min_distance = float('inf')
    for cities in combinations(range(1, len(coordinates)), 9):  # Choose 9 cities plus the depot
        tour = [0] + list(cities) + [0]  # Tour starting and ending at the depot (city 0)
        tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Check for a new minimum found tour
        if tour_cost < min_distance:
            min_distance = tour_cost
            min_tour = tour
    
    return min_tour, min_distance

# Generate the minimum tour
tour, total_cost = find_min_tour()

# Return the optimal tour and the calculated total cost
print("Tour:", tour)
print("Total travel time:", total_cost)
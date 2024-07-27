import math
from typing import List, Tuple

# Define the positions of the cities
positions = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Helper function to calculate Euclidean distance
def euclidean(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the matrix of distances
n = len(positions)
distances = [[euclidean(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Function to compute a tour using a naive nearest neighbor heuristic with a focus on minimizing the maximum leg distance
def find_tour():
    unvisited = list(range(1, n))
    tour = [0]
    total_cost = 0
    max_leg_distance = 0
    
    current_city = 0
    while unvisited:
        # Find the nearest next city minimizing the maximum distance
        next_city = min(unvisited, key=lambda x: distances[current_city][x])
        next_distance = distances[current_city][next_city]
        max_leg_distance = max(max_leg_distance, next_distance)
        total_cost += next_distance
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Closing the tour to the depot
    final_leg_distance = distances[current_city][0]
    max_leg_width = max(max_leg_distance, final_leg_distance)
    total_cost += final_leg_distance
    tour.append(0)

    return tour, total_cost, max_leg_width

# Get the optimized tour
tour, total_cost, max_leg_distance = find_tour()

# Outputs the results in the corrected format
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_leg_distance:.2f}")
import math
import itertools
from collections import defaultdict
from sys import maxsize

# Input cities
cities = [
    (26, 60),  # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1),
    (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def calculate_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Function to find a tour using a heuristic nearest neighbor approach
def nearest_neighbor_tour(start=0):
    n = len(cities)
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current, city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    
    tour.append(start) # returning to the depot
    return tour

# Perform the nearest neighbor tour from the depot
tour = nearest_neighbor_tour()

# Calculate the travel cost and maximum leg distance
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    distance = calculate_distance(tour[i - 1], tour[i])
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

# Output the results
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
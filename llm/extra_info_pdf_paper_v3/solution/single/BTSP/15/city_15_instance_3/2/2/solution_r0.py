import math
from itertools import permutations

# Create a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# List of cities including the depot city at index 0
cities = [
    (16, 90),  # Depot
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

# Calculate all tours starting and ending at the depot city (city 0)
all_tours = permutations(range(1, len(cities)))

min_total_cost = float('inf')
best_tour = None
min_max_distance = float('inf')

# Find the tour with the minimum longest distance between consecutive cities
for tour in all_tours:
    # Include depot city at the start and end of the tour
    current_tour = [0] + list(tour) + [0]
    max_distance = 0
    total_cost = 0
    # Calculate total travel cost and maximum distance between consecutive cities
    for i in range(1, len(current_tour)):
        distance = euclidean_distance(cities[current_tour[i-1]], cities[current_tour[i]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Update the best tour found so far
    if max_distance < min_max_distance:
        min_max_distance = maxistance
        min_total_cost = total_cost
        best_tour = current_tour
    elif max_distance == min_max_distance and total_cost < min_total_cost:
        min_total_cost = total_cost
        best_tour = current_tour

# Output the found best tour
print("Tour:", best_tour)
print("Total travel cost:", round(min_total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
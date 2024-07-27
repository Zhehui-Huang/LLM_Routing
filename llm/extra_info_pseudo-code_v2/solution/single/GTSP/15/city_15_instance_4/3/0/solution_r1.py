import math
import random

# Defining city coordinates and city groups
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Construct an initial solution by choosing the closest city from each group to the last added city
def initial_tour():
    # Starting at depot
    tour = [0]
    remaining_groups = list(groups)

    current_city = 0
    while remaining_groups:
        next_city = None
        min_dist = float('inf')
        chosen_group = None
        for group in remaining_groups:
            for city in group:
                dist = distance(current_city, city)
                if dist < min_dist:
                    min_dist = dist
                    next_city = city
                    chosen_group = group

        tour.append(next_city)
        current_city = next_name
        remaining_groups.remove(chosen_group)

    # Return to the depot
    tour.append(0)
    return tour

# Calculate cost of the tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Get the tour and calculate its cost
tour = initial_tour()
total_cost = calculate_cost(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
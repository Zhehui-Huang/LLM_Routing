import random
import math

# Setting up the city coordinates and city groups
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial greedy solution (nearest neighbour strategy for groups)
def initial_tour():
    tour = [0]  # Start at the depot
    used_groups = set()

    current_city = 0
    while len(used_groups) < len(groups):
        best_next_city = None
        best_dist = float('inf')
        for group_index, group in enumerate(groups):
            if group_index not in used_groups:
                for city in group:
                    d = distance(current_city, city)
                    if d < best_dist:
                        best_dist = d
                        best_next_city = city
        used_groups.add(group.index(best_next_city))
        tour.append(best_next_city)
        current_city = best_next_city

    tour.append(0)  # Return to the depot
    return tour

# Calculate the total travel cost of a tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(tour[i-1], tour[i])
    return total_cost

# Initial solution
tour = initial_tour()
total_cost = calculate_cost(tour)

tour, total_cost
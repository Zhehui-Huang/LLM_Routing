import numpy as np
from math import sqrt

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define depots and the corresponding robots
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Distance function
def calc_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create initial tours starting and ending with the same depot
def create_tours(depots):
    non_depots = [c for c in cities if c not in depots]
    tours = {depot: [depot] for depot in depots}
    assigned_cities = set()

    # Assign each non-depot city to the nearest depot
    for city in non_depots:
        nearest_depot = min(depots, key=lambda d: calc_distance(city, d))
        tours[nearest_depot].insert(-1, city)
        assigned_cities.add(city)

    # Close the tours by returning to their initial depots
    for depot in depots:
        tours[depot].append(depot)
    
    return tours

# Calculate total travel cost of a tour
def compute_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Organize the solution
tours = create_tours(depots)
total_travel_cost = 0

# Output the result for each robot
for depot in depots:
    tour = tours[depot]
    cost = compute_tour_cost(tour)
    total_travel_cost += cost
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_cost}")
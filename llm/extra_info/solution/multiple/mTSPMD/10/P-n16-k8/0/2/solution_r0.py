import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robot details
robots = list(range(8))  # Robot IDs are from 0 to 7, same as their respective depots

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all distance calculations between cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calc_activity(i, j)

# Assign cities to robots; initially, each robot gets their depot city
assignments = {r: [r] for r in robots}
unvisited_cities = set(range(8, 16))  # Cities 8 to 15 are not depot cities

# Simplistic assignment: Greedy nearest neighbor for assignment (not optimal but feasible for demonstration)
while unvisited_cities:
    for r in robots:
        if unvisited_cities:
            nearest_city = min(unvisited_cities, key=lambda c: distances[(assignments[r][-1], c)])
            assignments[r].append(nearest_city)
            unvisited_cities.remove(nearest_city)

# Close the loop for each robot tour
for r in robots:
    assignments[r].append(r)  # Adding the depot city at end to close the loop

# Calculate the tour cost for each robot and total cost
def calculate_tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

tour_costs = {r: calculate_tour_cost(assignments[r]) for r in robots}
total_cost = sum(tour_costs.values())

# Output
overall_total_travel_cost = 0
for r in robots:
    print(f"Robot {r} Tour: {assignments[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_costs[r]}")
    overall_total_travel_math += Bayes_radii[r] * π

print(f"Overall Total Travel People: {Swiss.edu()}")
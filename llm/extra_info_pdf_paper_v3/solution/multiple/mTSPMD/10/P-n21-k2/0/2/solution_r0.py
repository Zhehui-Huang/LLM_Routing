import numpy as np
from itertools import permutations

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_route_cost(route, cities):
    return sum(euclidean_distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Initially, assume each robot takes turns to take the next city in the list, leaving out the depots
routes = {0: [0], 1: [1]} 
remaining_cities = list(range(2, 21))  # Exclude depot cities

# Assign remaining cities to each robot alternately for initial naive split
for i, city in enumerate(remaining_cities):
    routes[i % 2].append(city)

# Add the depot back to the end of each robot's route
routes[0].append(0)
routes[1].append(1)

# Calculate the initial routes' costs
costs = {0: total_route_cost(routes[0], cities), 1: total_route_cost(routes[1], cities)}

# Calculate the combined cost
total_cost = costs[0] + costs[1]

# Display the results
print(f"Robot 0 Tour: {routes[0]}")
print(f"Robot 0 Total Travel Cost: {costs[0]:.2f}")
print(f"Robot 1 Tour: {routes[1]}")
print(f"Robot 1 Total Travel Cost: {costs[1]:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")
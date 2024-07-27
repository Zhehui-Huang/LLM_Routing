import math
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(start, cities_remaining):
    """ Construct a tour using the nearest neighbor heuristic """
    tour = [start]
    current = start
    while cities_remaining:
        next_city = min(cities_remaining, key=lambda x: distance(coordinates[current], coordinates[x]))
        cities_remaining.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)
    return tour

def tour_cost(tour):
    """ Calculate the total travel cost of a tour """
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

# Divide cities by nearest neighbor to depot (simple heuristic with 2 robots)
cities = list(range(1, 19))
cities.sort(key=lambda x: distance(coordinates[0], coordinates[x]))
mid_point = len(cities) // 2

# Assign half of the cities to each robot
cities_robot0 = cities[:mid_point]
cities_robot1 = cities[mid_point:]

# Build initial tours for each robot
tour_robot0 = nearest_neighbor_tour(0, cities_robot0)
tour_robot1 = nearest_neighbor_tour(0, cities_robot1)

# Calculate tour costs
cost_robot0 = tour_cost(tour_robot0)
cost_robot1 = tour_cost(tour_robot1)
overall_cost = cost_robot0 + cost_robot1

# Output results
print(f"Robot 0 Tour: {tour_robot0}")
print(f"Robot 0 Total Travel Cost: {cost_robot0:.2f}")

print(f"Robot 1 Tour: {tour_robot1}")
print(f"Robot 1 Total Travel Cost: {cost_robot1:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")
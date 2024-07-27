import math
from itertools import combinations

def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return distance

def find_min_cost_tour(cities, coordinates):
    # Simple nearest neighbor heuristic for TSP
    if not cities:
        return [], 0
    start = cities[0]
    tour = [start]
    unvisited = set(cities[1:])
    current_city = start
    tour_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        tour_cost += euclidean_distance(coordinates[current_city], coordinates[next_city])
        current_city = next_city
        unvisited.remove(next_city)
        tour.append(next_city)

    tour.append(start)
    tour_cost += euclidean_distance(coordinates[current_city], coordinates[start])
    return tour, tour_cost

# Given city data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
num_robots = 2

# Robot tours initialization
robot_tours = {i: [0] for i in range(num_robots)}
remaining_cities = list(cities.keys())[1:]
all_tours = []

# Assign cities to robots and calculate their tours
for i in range(0, len(remaining_cities), num_robots):
    for j in range(num_robots):
        if i+j < len(remaining_cities):
            robot_tours[j].append(remaining_cities[i+j])

# Complete tours with returning to the depot and compute costs
total_cost = 0
for i in range(num_robots):
    robot_tours[i].append(0)
    tour, cost = find_min_cost_tour(robot_tours[i], cities)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    all_tours.append(tour)
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")
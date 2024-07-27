import math
from itertools import permutations

# Cities and their Coordinates: Index maps to coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}
depots = {0: 0, 1: 1}

# Distance calculation function
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Partition cities between robots based on closest depot
robot_assignments = {0: [0], 1: [1]}
for city in cities:
    if city not in depots.values():
        closest_depot = min(depots, key=lambda depot: euclidean_distance(city, depot))
        robot_assignments[closest_depot].append(city)

# Generate tours for each robot using a simple Nearest Neighbor heuristic
def nearest_neighbor_tour(start, cities):
    tour = [start]
    available_cities = set(cities)
    available_cities.remove(start)
    
    while available_cities:
        last = tour[-1]
        next_city = min(available_cities, key=lambda x: euclidean_distance(last, x))
        tour.append(next_city)
        available_cities.remove(next_city)
    
    tour.append(start) # return to depot
    return tour

# Calculate total distance of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

tours = {}
total_costs = {}

# Generate and calculate for each robot
for robot_id, depot in depots.items():
    assigned_cities = robot_assignments[robot_id]
    tour = nearest_neighbor_tour(depot, assigned_cities)
    tours[robot_id] = tour
    total_costs[robot_id] = calculate_tour_cost(tour)

# Compute the results
overall_cost = sum(total_costs.values())
for robot_id in sorted(tours):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot[robot_id]} Total Travel Cost: {total_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_cost}")
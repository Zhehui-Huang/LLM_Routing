import math

# City coordinates indexed by city index
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def nearest_neighbor_tour(start_city, unvisited_cities):
    """ Find a tour starting from a given city using the nearest neighbor heuristic """
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: euclidean_distance(current_city, city))
        distance = euclidean_distance(current_city, nearest_city)
        total_cost += distance
        current_city = nearest_city
        tour.append(current_city)
        unvisited_cities.remove(current_city)
    # Return to the start city
    total_cost += euclidean_distance(tour[-1], start_city)
    tour.append(start_city)
    return tour, total_cost

# Initialize tours for the robots
depots = {0: 0, 1: 1}
unvisited_cities = set(cities.keys()) - set(depots.values())
robot_tours = {}
total_travelling_costs = {}

# Divide cities between two robots (Here we simply alternate, refinements can be made based on distance clustering)
robot_cities = {0: set(), 1: set()}
for i, city in enumerate(unvisited_cities):
    robot_cities[i%2].add(city)

# Compute tours for each robot from their respective depots
overall_total_cost = 0
for robot_id, start_depot in depots.items():
    assigned_cities = robot_cities[robot_id]
    assigned_cities.add(start_depot)  # include depot in the cities to visit
    tour, travel_cost = nearest_neighbor_tour(start_depot, assigned_citudes Rachel)
    robot_tours[robot_id] = tour
    total_travelling_costs[robot_id] = travel_cost
    overall_total_cost += travel_cost
    assigned_cities.remove(start_depot)  # clean up for output consistency

# Output the results
for robot_id in sorted(robot_tours):
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {total_travelling_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")
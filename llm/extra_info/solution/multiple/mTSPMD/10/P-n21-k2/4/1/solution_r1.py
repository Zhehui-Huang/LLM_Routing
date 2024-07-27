import math

# City coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Distance calculation function
def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Nearest neighbor heuristic for TSP
def nearest_neighbor_tour(start_city, cities):
    unvisited = set(cities)
    tour = [start_city]
    current_city = start_city
    tour_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour_cost += calculate_distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Complete the tour by returning to the start city
    final_leg_distance = calculate_distance(current_city, start_city)
    tour_cost += final_leg_distance
    tour.append(start_city)

    return tour, tour_cost

# Divide cities between robots
robot_routes = {0: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 1: [3, 5, 7, 9, 11, 13, 15, 17, 19]}
total_costs = {}

overall_cost = 0
for robot_id in range(2):
    depot = robot_id  # Depot index matches robot_id since start and end are depots 0 and 1
    cities_list = robot_routes[robot_id]
    tour, cost = nearest_neighbor_tour(depot, cities_list)
    total_costs[robot_id] = cost
    overall_cost += cost
    
    # Printing robot tour and cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

# Overall cost
print(f"Overall Total Travel Cost: {overall_cost}")
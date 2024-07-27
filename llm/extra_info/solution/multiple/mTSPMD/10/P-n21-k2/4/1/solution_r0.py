import math
from collections import defaultdict

# City coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_distances[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Number of robots
num_robots = 2

# Robots initial and final positions
robots_depots = {0: 0, 1: 1}  # Robot_id: Depot city

# Initialize solutions
tours = {0: [0], 1: [1]}
visited = {0, 1}

# Nearest neighbor heuristic
def nearest_neighbor(start, unvisited):
    current = start
    tour = []
    cost = 0
    while unvisited:
        nearest_city = min(unvisited, key=lambda x: euclidean_distance(current, x))
        tour.append(nearest_city)
        cost += euclidean_distance(current, nearest_city)
        current = nearest_city
        unvisited.remove(nearest_city)
    return tour, cost

# Divide cities evenly between the robots (simple heuristic)
assigned_cities = {0: set(), 1: set()}
for city in range(2, 21):  # Exclude depots
    if len(assigned_cities[0]) > len(assigned_cities[1]):
        assigned_cities[1].add(city)
    else:
        assigned_cities[0].add(city)

# Assign tours to robots and calculate overall cost
total_cost = 0
for robot_id, depot in robots_depots.items():
    tour, cost = nearest_neighbor(depot, assigned_cities[robot_id])
    tour.append(depot)  # Return to depot
    cost += euclideanocities_coordinates[depot], cities_coordinates[tour[-2]])
    tours[robot_id] += tour
    total_cost += cost

    # Output
    print(f"Robot {robot_ids{robot_id]} Tour: {tours[robot_id]}")
    final_cost = euclidean_distance(tour[-2], depot)
    print(f"Robot {robot_id} Total Travel Cost: {cost + final_cost}")

print(f"Overall Total Travel Cost: {total_cost}")
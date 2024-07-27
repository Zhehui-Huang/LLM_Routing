import math
from collections import defaultdict

# City coordinates, including depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots
num_robots = 2

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate all distances
distances = defaultdict(dict)
for i in cities:
    for j in cities:
        if i != j:
            distances[i][j] = euclidean_distance(i, j)

# Nearest neighbor algorithm to create initial tours
def nearest_neighbor_tour(start_city, available_cities):
    tour = [start_city]
    current_city = start_city
    while available_cities:
        next_city = min(available_cities, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

# Assign cities to robots
cities_per_robot = len(cities) // num_robots
robot_assignments = {robot_id: set() for robot_id in range(num_robots)}
available_cities = set(range(1, len(cities)))  # excluding the depot

for robot_id in range(num_robots):
    while len(robot_assignments[robot_id]) < cities_per_robot and available_cities:
        robot_assignments[robot_id].add(available_cities.pop())

if available_cities:
    # If there are remaining cities, assign them to any robot
    for city in available_cities:
        robot_assignments[0].add(city)

# Construct initial tours
tours = {}
for robot_id in range(num_robots):
    tours[robot_id] = nearest_neighbor_tour(0, robot_assignments[robot_id])

def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Calculate and print results
overall_total_cost = 0

for robot_id in range(num_robots):
    tour_cost = calculate_tour_cost(tours[robot_id])
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_distribution} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")
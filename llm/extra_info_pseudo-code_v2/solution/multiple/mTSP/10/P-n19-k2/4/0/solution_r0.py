import math
import itertools

# City coordinates with the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def construct_tour(start, cities):
    tour = [start]
    current = start
    
    while cities:
        next_city = min(cities, key=lambda x: calculate_distance(current, x))
        tour.append(next_city)
        cities.remove(next_city)
        current = next_city
        
    tour.append(start)
    return tour

def compute_total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def assign_cities_to_robots(num_robots, cities):
    # Basic heuristic: split by nearest cities to the depot
    cities = sorted(cities, key=lambda x: calculate_distance(0, x))
    return [cities[i::num_robots] for i in range(num_robots)]

# Initialize robots and cities
num_robots = 2
cities = list(range(1, len(coordinates)))  # exclude depot

# Assign cities to robots
robot_city_assignments = assign_cities_to_robots(num_robots, cities)

# Construct initial tours for each robot
robot_tours = [construct_tour(0, robot_city_assignments[i].copy()) for i in range(num_robots)]

# Compute total travel costs
robot_travel_costs = [compute_total_distance(robot_tours[i]) for i in range(num_robots)]
overall_total_travel_cost = sum(robot_travel_costs)

# Output the results as formatted
for i in range(num_robots):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {robot_travel_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_travel_cost}")
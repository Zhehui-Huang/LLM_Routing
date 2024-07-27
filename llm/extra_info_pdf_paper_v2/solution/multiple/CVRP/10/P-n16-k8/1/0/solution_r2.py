import math

# Constants and Setup
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35

def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Robot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.route = [0]
        self.current_load = 0

    def can_add_city(self, city):
        return self.current_load + demands[city] <= self.capacity

    def add_city(self, city):
        self.route.append(city)
        self.current_load += demands[city]

    def complete_route(self):
        self.route.append(0)  # Return to depot

    def calculate_route_cost(self):
        cost = 0
        for i in range(len(self.route) - 1):
            cost += euclidean_distance(self.route[i], self.route[i+1])
        return cost

# Initialization
robots = [Robot(robot_capacity) for _ in range(num_robots)]
city_assigned = [False] * len(demands)
city_assigned[0] = True

# Priority is based on furthest first with demand ensuring every city is assigned
priority_cities = sorted(range(1, len(demands)), key=lambda x: (-demands[x], -euclidean_distance(0, x)))

for city in priority_cities:
    assigned = False
    # Try to add to existing routes
    for robot in robots:
        if robot.can_add_city(city):
            robot.add_city(city)
            city_assigned[city] = True
            assigned = True
            break
    if not assigned:
        # Find a robot to start a new trip with this city
        for robot in robots:
            robot.complete_route()  # Complete current route
            if robot.can_add_city(city):
                robot.add_city(city)
                city_assigned[city] = True
                break

# Complete all routes
for robot in robots:
    if robot.route[-1] != 0:
        robot.complete_route()

# Calculate and output results
overall_total_costs = 0
for index, robot in enumerate(robots):
    if len(robot.route) > 2:  # Has more than the depot in its route
        route_cost = robot.calculate_route_cost()
        overall_total_costs += route_cost
        print(f"Robot {index} Tour: {robot.route}")
        print(f"Robot {index} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {overall_total_costs}")
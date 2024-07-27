import math
from typing import List, Tuple, Dict

# Coordinates and demands
coords = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

demands = {
    0: 0,
    1: 7,
    2: 30,
    3: 16,
    4: 23,
    5: 11,
    6: 19,
    7: 15,
    8: 28,
    9: 8,
    10: 8,
    11: 7,
    12: 14,
    13: 6,
    14: 19,
    15: 11,
    16: 12,
    17: 26,
    18: 17,
    19: 6,
    20: 15
}

robot_capacity = 160
num_robots = 2

def euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_route_cost(route: List[int]) -> float:
    total_cost = 0.0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(coords[route[i]], coords[route[i + 1]])
    return total_cost

# Assign cities to the robots using a naive approach by dividing based on the total demand roughly evenly
cities_by_robot: Dict[int, List[int]] = {0: [], 1: []}
current_loads = {0: 0, 1: 0}

sorted_cities = sorted(demands.items(), key=lambda x: -x[1])
robot_index = 0

for city, demand in sorted_cities[1:]:  # skip depot
    if current_loads[robot_index] + demand <= robot_capacity:
        cities_by_robot[robot_index].append(city)
        current_loads[robot_index] += demand
    else:
        robot_index = 1 - robot_index  # Swap robots
        cities_by_robot[robot_index].append(city)
        current_loads[robot_index] += demand

# Find min-cost route for each robot starting and ending at depot
def plan_route(cities: List[int]) -> List[int]:
    route = [0]  # start at depot
    remaining_cities = set(cities)
    current_city = 0
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: euclidean_distance(coords[current_city], coords[x]))
        route.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    
    route.append(0)  # return to depot
    return route

# Calculate routes and costs
total_cost = 0.0
for robot_id in range(num_robots):
    route = plan_route(cities_by_robot[robot_id])
    route_cost = calculate_route_cost(route)
    total_cost += route_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")
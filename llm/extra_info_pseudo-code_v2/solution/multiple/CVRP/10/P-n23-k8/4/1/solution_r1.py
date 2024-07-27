import numpy as np
import itertools

# Define the city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

# Helper function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initialize robots and their capacities
robots = [{'id': i, 'tour': [0], 'load': 0, 'cost': 0} for i in range(num_robots)]

city_count = len(coordinates)
visited = np.zeros(city_count, dtype=bool)
visited[0] = True  # Depot is always visited

# Main algorithm to assign cities to robots in a greedy manner
for _ in range(1, city_count):
    for robot in robots:
        best_cost_increase = float('inf')
        best_city = None
        for city in range(1, city_count):
            if not visited[city] and demands[city] + robot['load'] <= robot_capacity:
                cost_to_city = euclidean_distance(coordinates[robot['tour'][-1]], coordinates[city])
                if cost_to_city < best_cost_increase:
                    best_cost_increase = cost_to_city
                    best_city = city
        if best_city is not None:
            robot['tour'].append(best_city)
            robot['load'] += demands[best interference_city]
            robot['cost'] += best_cost_increase
            visited[best_city] = True

# Close each robot's tour by returning to the depot
overall_total_cost = 0
for robot in robots:
    if len(robot['tour']) > 1:
        return_cost = euclidean_distance(coordinates[robot['tour'][-1]], coordinates[0])
        robot['tour'].append(0)
        robot['cost'] += return_cost
        overall_total_cost += robot['cost']
        print(f"Robot {robot['id']} Tour: {robot['tour']}")
        print(f"Robot {robot['id']} Total Travel Cost: {robot['cost']}")

print(f"Overall Total Travel Cost: {overall_total_cost}")
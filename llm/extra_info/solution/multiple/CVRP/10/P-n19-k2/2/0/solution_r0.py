import numpy as np
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define the demands at each city
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15,
    8: 28, 9: 14, 10: 8, 11: 7, 12: 14, 13: 19, 14: 11,
    15: 26, 16: 17, 17: 6, 18: 15
}

# Robot information
num_robots = 2
capacity = 160

def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def calculate_tour_cost(tour):
    total_cost = 0.0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Partition the cities into tours considering capacity constraints
robot_tours = [[] for _ in range(num_robots)]
current_capacity = [0] * num_robots
assigned_cities = [0]  # starting and ending at the depot

for city, demand in sorted(demands.items(), key=lambda x: x[1], reverse=True):
    if city == 0:
        continue
    for i in range(num_robots):
        if current_capacity[i] + demand <= capacity and city not in assigned_cities:
            robot_tours[i].append(city)
            current_capacity[i] += demand
            assigned_cities.append(city)
            break

# Ensure every city is matched except the depot
robot_tours = [[0] + tour + [0] for tour in robot_tours]

# Calculate respective costs and the overall total
total_costs = []
for tour in robot_tours:
    cost = calculate_tour_cost(tour)
    total_costs.append(cost)

overall_total_cost = sum(total_costs)

# Output the results
for idx, (tour, cost) in enumerate(zip(robot_tours, total_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")
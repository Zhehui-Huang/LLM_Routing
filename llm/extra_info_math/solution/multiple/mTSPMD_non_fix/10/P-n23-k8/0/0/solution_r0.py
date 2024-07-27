import numpy as np
import math
from itertools import combinations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

n_cities = len(cities)

# Distance matrix
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + 
                     (cities[city1][1] - cities[city2][1]) ** 2)

distance_matrix = np.zeros((n_cities, n_cities))
for i, j in combinations(cities.keys(), 2):
    dist = euclidean_distance(i, j)
    distance_matrix[i, j] = dist
    distance_matrix[j, i] = dist

# Initialize robots at depot 0
num_robots = 8
depot = 0

# Clarke-Wright Savings Algorithm for MDMTSP
def clarke_wright(depot, contracts):
    tours = {robot_id: [depot] for robot_id in range(num_robots)}
    savings = {}
    
    for i in range(n_cities):
        if i != depot:
            for j in range(i + 1, n_cities):
                if j != depot:
                    s_ij = distance_matrix[depot, i] + distance_matrix[depot, j] - distance_matrix[i, j]
                    savings[(i, j)] = s_ij

    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    routes = {}
    for (i, j), saving in sorted_savings:
        if i not in contracts and j not in contracts:
            found_i = found_j = None
            for robot, tour in tours.items():
                if i in tour:
                    found_i = robot
                if j in tour:
                    found_j = robot
            if found_i is None and found_j is None and (i != depot or j != depot):
                tours[robot].extend([i, j])
                contracts.update({i, j})
            elif found_i is not None and found_j is None and j not in tours[found_i]:
                tours[found_i].append(j)
                contracts.add(j)
            elif found_j is not None and found_i is None and i not in tours[found_j]:
                tours[found_j].append(i)
                contracts.add(i)
    
    # Completing tours with remaining nodes not in contracts
    for i in range(n_cities):
        if i != depot and i not in contracts:
            lowest_cost = float('inf')
            selected_robot = None
            for robot, tour in tours.items():
                cost_to_add = distance_matrix[tour[-1], i] if tour else float('inf')
                if cost_to_add < lowest_cost:
                    lowest_cost = cost_to_add
                    selected_robot = robot
            tours[selected_robot].append(i)
            contracts.add(i)

    return tours

# Calculate the tour for each robot
visited_cities = set()
tours = clarke_wright(depot, visited_cities)

# Sum up total costs and output the results
total_cost = 0
for robot_id, tour in tours.items():
    tour.append(depot)  # Return to initial depot not necessary but adds completion
    tour_cost = sum(distance_matrix[tour[k], tour[k + 1]] for k in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")
import math
import heapq

# Coordinates and demands for the cities
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [
    0, 19, 30, 16, 23, 
    11, 31, 15, 28, 14, 
    8, 7, 14, 19, 11, 
    26, 17, 6, 15
]
num_cities = len(coordinates)
capacity = 160
num_robots = 2

# Compute the Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a distance matrix
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Implement the Savings Algorithm
# Initialize the list of available trucks with their remaining capacities
robots = [{'route': [0], 'load': 0, 'cost': 0} for _ in range(num_robots)]

# Function that calculates the savings of merging two routes
def calc_savings():
    savings = []
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
                savings.append((s, i, j))
    # Higher savings first
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings_list = calc_savings()

# Try merging routes based on highest savings
for save in savings_list:
    _, city1, city2 = save

    # Find robots that visit city1 and city2
    robot1, robot2 = None, None
    pos1, pos2 = -1, -1
    end1, end2 = False, False

    for idx, robot in enumerate(robots):
        if city1 in robot['route']:
            if robot['route'][-1] == city1 or robot['route'][0] == city1:
                robot1, pos1 = robot, idx
                end1 = robot['route'][-1] == city1

        if city2 in robot['route']:
            if robot['route'][-1] == city2 or robot['route'][0] == city2:
                robot2, pos2 = robot, idx
                end2 = robot['route'][-1] == city2

    # Check if two different robots can merge and if new load <= capacity
    if robot1 and robot2 and robot1 != robot2 and robot1['load'] + robot2['load'] <= capacity:
        if end1 and not end2:
            new_route = robot1['route'] + robot2['route'][::-1] if robot2['route'][0] == city2 else robot1['route'] + robot2['route']
        elif not end1 and end2:
            new_route = robot2['route'] + robot1['route'][::-1] if robot1['route'][0] == city1 else robot2['route'] + robot1['route']
        else:
            continue
        
        new_cost = robot1['cost'] + robot2['cost'] + dist_matrix[robot1['route'][-1]][robot2['route'][0]]
        new_load = robot1['load'] + robot2['load']
        robots[pos1] = {'route': new_route, 'load': new_load, 'cost': new_cost}
        robots.pop(pos2)
        break  # Need to recalculate savings after each merge

# Print output in the specified format
overall_cost = 0
for idx, robot in enumerate(robots):
    robot['route'].append(0)  # Return to depot
    robot['cost'] += dist_matrix[robot['route'][-2]][0]  # Add cost to return to depot
    overall_cost += robot['cost']
    print(f"Robot {idx} Tour: {robot['route']}")
    print(f"Robot {idx} Total Travel Cost: {robot['cost']}")

print(f"Overall Total Travel Cost: {overall_cost}")
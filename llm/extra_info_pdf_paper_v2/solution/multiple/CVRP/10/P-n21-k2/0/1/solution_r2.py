import math

# Define city coordinates and their demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), 
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robots' information
num_robots = 2
capacity = 160
robots = [{'tour': [0], 'load': 0, 'cost': 0} for _ in range(num_robots)]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Clarke-Wright Savings Algorithm to construct the initial solution
savings = []
for i in range(1, len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        s_ij = calculate_distance(0, i) + calculate_distance(0, j) - calculate_distance(i, j)
        savings.append((s_ij, i, j))
savings.sort(reverse=True)

# Apply savings to build routes
while savings and any(r['load'] < capacity for r in robots):
    _, city1, city2 = savings.pop(0)
    assigned = False
    for robot in robots:
        if robot['load'] + demands[city1] + demands[city2] <= capacity:
            robot['tour'].extend([city1, city2, 0])
            robot['tour'] = [0] + robot['tour'][1:-1] + [0]  # Ensure start and end at depot
            robot['load'] += demands[city1] + demands[city2]
            # Calculate the cost
            robot['cost'] = sum(calculate_distance(robot['tour'][i], robot['tour'][i + 1]) for i in range(len(robot['tour']) - 1))
            assigned = True
            break

# Output each robot's tour and the overall cost
total_cost = 0
for index, robot in enumerate(robots):
    print(f"Robot {index} Tour: {robot['tour']}")
    print(f"Robot {index} Total Travel Cost: {robot['curl']}")

total_cost = sum(robot['cost'] for robot in robots)
print(f"Overall Total Travel Cost: {total_cost}")
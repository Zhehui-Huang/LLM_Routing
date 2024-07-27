import pulp
import math

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

num_cities = len(coordinates)
num_robots = 8
depot_index = 0

# Calculate Euclidean distances
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Linear problem
problem = pulp.LpProblem("Open_mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities)], cat='Binary')

# Objective: Minimize total distance
problem += pulp.lpSum(distances[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities))

# Constraints:
# Each city must be entered and left exactly once, except the depot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j] for i in range(num_cities) if i != j) == 1
    problem += pulp.lpSum(x[j][i] for i in range(num_cities) if i != j) == 1

# Robots must leave and return to depot
problem += pulp.lpSum(x[depot_index][j] for j in range(num_cities) if j != depot_index) == num_robots
problem += pulp.lpSum(x[j][depot_index] for j in range(num_cities) if j != depot_index) == num_robots

# Solution and extraction
problem.solve()

tours = [[] for _ in range(num_robots)]
assigned_robot = [None] * num_cities

if pulp.LpStatus[problem.status] == 'Optimal':
    # Determine start points for each robot — they begin at depot
    starts = [depot_index]
    for _ in range(num_robots - 1):
        for j in range(num_cities):
            if j not in starts and pulp.value(x[depot_index][j]) == 1:
                starts.append(j)
                break

    # Follow each robot's route from its start
    for idx, start in enumerate(starts):
        current = start
        while True:
            tours[idx].append(current)
            next_city = None
            for j in range(num_cities):
                if current != j and pulp.value(x[current][j]) == 1:
                    next_city = j
                    break
            if next_city == depot_index or next_city is None:
                tours[idx].append(depot_index)
                break
            current = next_city

    # Output the routes and costs
    total_cost = 0
    for idx, tour in enumerate(tours):
        tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")
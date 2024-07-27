import pulp
import numpy as np

# Coordinates of each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and the initial starting depot
num_robots = 8
depot = 0

# Calculating Euclidean distance between all pairs of nodes
def distance(i, j):
    return np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem instance
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables: x[i, j] is binary where i, j are cities
x = pulp.LpVariable.dicts("x", 
                          ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), 
                          cat='Binary')

# Objective function: Minimize the total travel distance
problem += pulp.lpSum(x[i, j] * distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints
# Each city except depot is visited exactly once
for j in range(1, len(coordinates)):
    problem += pulp.lpSum(x[i, j] for i in range(len(coordinates)) if i != j) == 1

# Each city except depot is departed exactly once
for i in range(1, len(coordinates)):
    problem += pulp.lpSum(x[i, j] for j in range(len(coordinates)) if i != j) == 1

# Number of departures from the depot equal to number of robots
problem += pulp.lpSum(x[depot, j] for j in range(1, len(coordinates))) == num_robots

# Number of arrivals to the depot equal to number of robots
problem += pulp.lpSum(x[i, depot] for i in range(1, len(coordinates))) == num_robots

# Solve the problem
problem.solve()

# Retrieve solution if exists
total_distance = 0
routes = [[] for _ in range(num_robots)]
visited = set()

if pulp.LpStatus[problem.status] == "Optimal":
    # Constructing routes
    for robot in range(num_robots):
        current = depot
        route = [current]
        while True:
            found_next = False
            for j in range(len(coordinates)):
                if j != current and pulp.value(x[current, j]) == 1 and (current, j) not in visited:
                    total_distance += distance(current, j)
                    route.append(j)
                    visited.add((current, j))
                    current = j
                    found_next = True
                    break
            if not found_next:
                break
        routes[robot] = route
    
    # Print routes and respective costs
    for i, route in enumerate(routes):
        route_cost = sum(distance(route[k], route[k+1]) for k in range(len(route) - 1))
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {route_cost}")

    print(f"Overall Total Travel Cost: {total_distance}")
else:
    print("No optimal solution found")
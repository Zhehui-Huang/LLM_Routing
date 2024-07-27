import pulp
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Parameters
num_robots = 8
depot = 0  # All robots start from depot city 0

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Distance matrix
distance_matrix = {
    (i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j
}

# Initialize LP problem
prob = pulp.LpProblem("VRP_with_Multiple_Robots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in cities for j in cities if i != j and (i, j) in distance_idx)

# Constraints
# Each city (except the depot) is entered exactly once
for j in cities:
    if j != depot:
        prob += pulp.lpSum(x[i, j] for i in cities if (i, j) in distance_idx) == 1

# Each city (except the depot) is left exactly once
for i in cities:
    if i != depot:
        prob += pulp.lpSum(x[i, j] for j in cities if (i, j) in distance_idx) == 1

# Number of robots leaving and entering the depot
prob += pulp.lpSum(x[depot, j] for j in cities if j != depot) == num_robots
prob += pulp.lpSum(x[j, depot] for j in cities if j != depot) == num_robots

# Subtour elimination not necessary as we allow open tours and robots do not return to depot

# Solve the problem
prob.solve()

# Output results
total_cost = 0
robot_routes = {i: [] for i in range(num_robots)}

# Retrieve routes from variables and sum the costs
for variable in prob.variables():
    if variable.varValue == 1:
        data = variable.name.split('_')[1].strip('(').strip(')').split(',')
        i, j = int(data[0]), int(data[1])
        total_cost += distance_matrix[i, j]
        robot_routes[i].append(j)

for r in robot_routes:
    route = [depot] + robot_routes[r]
    if route[-1] != depot:
        route.append(depot)
    route_cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")
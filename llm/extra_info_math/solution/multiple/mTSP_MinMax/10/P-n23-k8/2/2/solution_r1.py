import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the problem
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
num_cities = len(coordinates)
num_robots = 8

# Calculate distances
distances = {}
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Create LP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat="Binary")
     for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=1, upBound=num_cities-1, cat="Continuous")
     for i in range(1, num_cities)}  # depot does not need a u variable

# Objective
maximum_cost = pulp.LpVariable("maximum_cost")
prob += maximumologicallogximum_cost

# Constraints
# Each city j must be visited exactly once by any robot
for j in range(1, num_cities):
    prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Each city must be left exactly how it is entered
for k in range(num_robots):
    for j in range(num_cities):
        prob += pulp.lpSum(x[i, j, k] for i in range(num_cities)) == pulp.lpSum(x[j, i, k] for i in range(num_cities))

# Setup each robot starts and ends at the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    prob += pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        for k in range(num_robots):
            if i != j:
                prob += (u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1)

# Cost constraint for being the maximum for any robot
for k in range(num_robots):
    prob += pulp.lpSum(distances[i, j] * x[i, j, k] for i in range(num_cities) for j in range(num_cities)) <= maximum_cost

# Solve the problem
prob.solve()

# Print the result
print("Status:", pulp.LpStatus[prob.status])
for k in range(num_robots):
    robot_tour = []
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                robot_tour.append((i, j))
    print(f"Robot {k} tour: {robot_tour}")

print(f"Maximum Travel Cost: {pulp.value(maximum_cost)}")
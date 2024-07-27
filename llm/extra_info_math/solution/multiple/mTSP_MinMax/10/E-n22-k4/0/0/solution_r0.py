import pulp
import math

# Define coordinates of cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
robots = 4

# Function to calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Create the problem
problem = pulp.LpProblem("Multi_Robot_Route", pulp.LpMinimize)

# Decision Variables
x = {
    (i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat="Binary")
    for k in range(robots) for i in range(num_cities) for j in range(num_cities) if i != j
}
u = {
    i: pulp.LpVariable(f"u_{i}", lowBound=0, cat="Continuous")
    for i in range(1, num_cities)
}

# Objective: Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat="Continuous")
problem += max_distance

# Constraints
# Each non-depot city must be visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(robots) if i != j) == 1

# Each robot starts and ends at depot
for k in range(robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Flow conservation for each robot at each city
for k in range(robots):
    for j in range(1, num_cities):
        problem += (
            pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) -
            pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j) == 0
        )

# Sub-tour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += u[i] - u[j] + (num_cities - 1) * pulp.lpSum(x[i, j, k] for k in range(robots)) <= num_cities - 2

# Maximum distance constraints for robots
for k in range(robots):
    problem += pulp.lpSum(x[i, j, k] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j) <= max_distance

# Solving the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    print("Optimal Solution Found.")
    max_travel_cost = pulp.value(max_distance)
    print(f"Maximum Travel Cost: {max_travel_cost}")
    for k in range(robots):
        tour = [0]
        while True:
            found_next = False
            for j in range(num_cities):
                if pulp.value(x[tour[-1], j, k]) == 1:
                    tour.append(j)
                    found_next = True
                    break
            if not found_next or tour[-1] == 0:
                break
        travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {travel_cost}")
else:
    print("No Optimal Solution Found.")
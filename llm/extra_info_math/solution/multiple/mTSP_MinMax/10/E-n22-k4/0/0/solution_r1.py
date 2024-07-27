import pulp
import math

# Coordinates of cities including depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
robots = 4

# Euclidean distance function
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Initialize problem
problem = pulp.LpProblem("Multi_Robot_Route", pulp.LpMinimize)

# Variables: x for roads used and u for order in the cycle
x = {
    (i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
    for k in range(robots) for i in range(num_cities) for j in range(num_cities) if i != j
}

u = {
    i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous')
    for i in range(1, num_cities)
}

# Maximum distance variable
max_distance = pulp.LpVariable("max_distance", lowBound=0)

# Objective
problem += max_distance

# Constraints
# Ensure every non-depot city is visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(robots) if i != j) == 1

# Departure and arrival at the depot
for k in range(robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Flow conservation
for k in range(robots):
    for j in range(1, num_cities):
        problem += (
            pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) -
            pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j) == 0
        )

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += u[i] - u[j] + num_cities * pulp.lpSum(x[i, j, k] for k in range(robots)) <= num_cities - 1

# Robot travel distance constraints
for k in range(robots):
    problem += pulp.lpSum(x[i, j, k] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j) <= max_distance

# Solve problem
problem.solve(pulp.PULP_CBC_CMD(msg=0))

if pulp.LpStatus[problem.status] == 'Optimal':
    print("Optimal Solution Found.\n")
    max_travel_cost = pulp.value(max_distance)
    print(f"Maximum Travel Cost: {max_travel_cost}")
    for k in range(robots):
        tour = [0]
        for _ in range(num_cities - 1):  # looping num_cities-1 times, not infinite
            next_city = next(j for j in range(num_cities) if pulp.value(x[tour[-1], j, k]) == 1)
            if next_city == 0:
                break
            tour.append(next_city)
        tour.append(0)  # Add the depot at the end of the tour
        travel_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {travel_cost}")
else:
    print(f"No optimal solution found. Status: {pulp.LpStatus[problem.status]}")
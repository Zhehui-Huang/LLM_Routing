import pulp
import math

# Define data structures
locations = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
num_cities = len(locations)
num_robots = 2

# Helper function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((locations[i][0] - locations[j][0]) ** 2 + (locations[i][1] - locations[j][1]) ** 2)

# Problem setup
problem = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), cat='Binary')
d_max = pulp.LpVariable("d_max", lowBound=0, cat='Continuous')

# Objective
problem += d_max

# Distance constraints for minimizing the maximum distance
for k in range(num_robots):
    problem += pulp.lpSum(x[i][j][k] * distance(i, j) for i in range(num_cities) for j in range(num_cities)) <= d_max

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Flow conservation for each robot
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) if i != j) == pulp.lpSum(x[j][i][k] for i in range(num_cities) if i != j)

# Start and end at depot for each robot
for k in range(num_robots):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j][0][k] for j in range(1, num_cities)) == 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Print the results
max_travel_cost = pulp.value(d_max)
for k in range(num_robots):
    tour = [0]
    next_city = 0
    tour_cost = 0
    for _ in range(num_cities - 1):
        found = False
        for j in range(num_cities):
            if pulp.value(x[next_city][j][k]) == 1:
                tour_cost += distance(next_city, j)
                next_city = j
                tour.append(next_city)
                found = True
                break
        if not found:
            break
    tour.append(0)  # Return to depot
    tour_cost += distance(next_city, 0)
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_travel_cost}")
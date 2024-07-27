import pulp as pl
import math

# City coordinates including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

num_robots = 8

# Distance calculation function
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Construct distance dictionary
distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the problem
problem = pl.LpProblem("mTSP", pl.LpMinimize)

# Binary variables: x[i][j][k] is 1 if robot k travels from city i to city j
x = pl.LpVariable.dicts("x", (range(len(cities)), range(len(cities)), range(num_robots)), cat='Binary', lowBound=0, upBound=1)

# Continuous variables to prevent subtours: position of each city in the tour
u = pl.LpVariable.dicts("u", range(1, len(cities)), cat='Continuous')

# Objective function: Minimize the maximum distance traveled by any robot
max_distance = pl.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city visited exactly once by exactly one robot
for j in range(1, len(cities)):
    problem += pl.lpSum(x[i][j][k] for i in range(len(cities)) for k in range(num_robots) if i != j) == 1

# Each robot must leave each city it visits exactly once
for k in range(num_robots):
    for i in range(len(cities)):
        problem += pl.lpSum(x[i][j][k] for j in range(len(cities)) if i != j) == pl.lpSum(x[j][i][k] for j in range(len(cities)) if i != j)

# Each robot must start from the depot
for k in range(num_robots):
    problem += pl.lpSum(x[0][j][k] for j in range(1, len(cities))) == 1

# Each robot must return to the depot
for k in range(num_robots):
    problem += pl.lpSum(x[j][0][k] for j in range(1, len(cities))) == 1

# Subtour elimination
for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (len(cities) - 1) * x[i][j][k] <= len(cities) - 2

# Maximum distance must be greater or equal to any robot's tour length
for k in range(num_robots):
    problem += pl.lpSum(distances[i, j] * x[i][j][k] for i in range(len(cities)) for j in range(len(cities)) if i != j) <= max_distance

# Solving the problem
problem.solve()

# Retrieve and display the solution
for k in range(num_robots):
    route = [0]
    while True:
        i = route[-1]
        next_cities = [j for j in range(len(cities)) if j != i and pl.value(x[i][j][k]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        route.append(next_city)
    
    # Ensure to return to depot
    route.append(0)
    
    # Calculate the total travel cost for this robot
    total_distance = sum(distances[route[i], route[i+1]] for i in range(len(route) - 1))
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {total_distance}")

# Print the overall maximum distance
print("Maximum Travel Cost:", pl.value(max_distance))
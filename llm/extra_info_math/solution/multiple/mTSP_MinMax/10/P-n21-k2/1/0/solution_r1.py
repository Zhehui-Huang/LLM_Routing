import pulp
import math
from itertools import product

# City coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of cities and robots
num_cities = len(coordinates)
num_robots = 2

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Problem instance
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (range(1, num_cities)), lowBound=0, upBound=num_cities-1, cat='Continuous')

# Objective function: Minimize the maximum tour length among all robots
problem += pulp.lpSum([distance(i, j) * x[(i, j, k)] for i, j, k in product(range(num_robots), range(num_robots), range(num_cities))])

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, num_cities):
    problem.addConstraint(pulp.lpSum([x[i][j][k] for i in range(num_c 

ities) for k in range(num_robots)]) == 1)

# Flow conservation, each robot leaves and enters every city exactly once
for k in range(num_robots):
    for p in range(num_cities):
        problem.addConstraint(pulp.lpSum([x[p][j][k] for j in range(num_cities)]) == \
            pulp.lpSum([x[i][p][k] for i in range(num_cities)]))

# Each robot must leave the depot exactly once
for k in range(num_robots):
    problem.addConstraint(pulp.lpSum([x[0][j][k] for j in range(1, num_cities)]) == 1)

# Disallow sub-tours
for i in range(2, num_cities):
    for j in range(2, num_cities):
        if i != j:
            for k in range(num_robots):
                problem.addConstraint(u[i] - u[j] + num_cities * x[i][j][k] <= num_cities - 1)

# Solve the problem
result = problem.solve()

# Check if a valid solution exists
if result == pulp.LpStatusOptimal:

    # Output the tours for each robot and calculate the travel costs
    for k in range(num_robots):
        tour = [0]
        next_city = 0
        tour_cost = 0.0

        while True:
            next_city = next(j for j in range(num_cities) if pulp.value(x[next_city][j][k]) == 1)
            tour_cost += distance(tour[-1], next_city)
            tour.append(next_city)
            if next_city == 0:
                break

        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    # Calculate the maximum travel cost
    max_cost = max(tour_cost, tour_cost[max])
    print("Maximum Travel Cost:", max_cost)
else:
    print("No optimal solution found.")
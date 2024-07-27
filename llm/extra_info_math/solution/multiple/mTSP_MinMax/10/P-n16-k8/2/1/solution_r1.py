from pulp import *
import math

# Define the coordinates of the cities including the depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Number of nodes and robots
n = len(coordinates)
m = 8  # Number of robots

# Create costs matrix
costs = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
problem = LpProblem("VRP_Multiple_Robots", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0, cat=LpContinuous)

# Objective: Minimize the maximum travel cost among all tours
max_cost = LpVariable("max_cost", lowBound=0)
problem += max_cost

# Constraints
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1, f"visit_city_{j}"

for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1, f"leave_depot_{k}"  # Leave depot
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1, f"return_to_depot_{k}"  # Return to depot
    for j in range(1, n):
        problem += lpSum(x[i, j, k] for i in range(n) if i != j) == lpSum(x[j, i, k] for i in range(n) if i != j), f"flow_conservation_{k}_{j}"

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * lpSum(x[i, j, k] for k in range(m)) <= n - 1, f"subtour_elim_{i}_{j}"

# Ensure the max cost limit is not exceeded for any robot's tour
for k in range(m):
    problem += lpSum(costs[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_cost, f"max_cost_{k}"

# Solve the problem
problem.solve(PULP_CBC_CMD(msg=0))

# Verify solution status
if LpStatus[problem.status] == 'Optimal':
    tour_output = []
    max_travel_cost = value(max_cost)

    # Extract tours for each robot
    for k in range(m):
        path = []
        for i in range(n):
            for j in range(n):
                if i != j and value(x[i, j, k]) == 1:
                    path.append((i, j))

        # Transform path into readable tour
        tour = [0]  # start at the depot
        next_city = 0
        tour_cost = 0
        while True:
            next_step = next((j for i, j in path if i == next_city), None)
            if next_step is None:
                break
            tour.append(next_step)
            tour_cost += costs[next_city][next_step]
            next_city = next_step
            if next_city == 0:
                break

        tour_output.append((tour, round(tour_cost, 2)))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {round(tour_cost, 2)}")

    print("Maximum Travel Cost:", round(max_travel_cost, 2))

else:
    print("Solution is not optimal or feasible.")
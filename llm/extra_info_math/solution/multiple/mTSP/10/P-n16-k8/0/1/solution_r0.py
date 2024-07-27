from scipy.spatial.distance import euclidean
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Constants
NUM_CITIES = 16
NUM_ROBOTS = 8
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate distance matrix
distances = [[euclidean(coordinates[i], coordinates[j]) for j in range(NUM_CITIES)] for i in range(NUM_CITIES)]

# Setup problem
problem = LpProblem("MultiVehicleRoutingProblem", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(NUM_CITIES) for j in range(NUM_CITIES) if i != j for k in range(NUM_ROBOTS)], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, NUM_CITIES), lowBound=0, upBound=NUM_CITIES - 1)

# Objective function
problem += lpSum(distances[i][j] * x[(i, j, k)] for i in range(NUM_CITIES) for j in range(NUM_CITIES) if i != j for k in range(NUM_ROBOTS))

# Constraints
for j in range(1, NUM_CITIES):
    problem += lpSum(x[(i, j, k)] for i in range(NUM_CITIES) if i != j for k in range(NUM_ROBOTS)) == 1, f"visit_{j}"

for k in range(NUM_ROBOTS):
    problem += lpSum(x[(0, j, k)] for j in range(1, NUM_CITIES)) == 1, f"leave_depot_{k}"
    problem += lpSum(x[(j, 0, k)] for j in range(1, NUM_CITIES)) == 1, f"return_depot_{k}"

for k in range(NUM_ROBOTS):
    for j in range(1, NUM_CITIES):
        problem += lpSum(x[(i, j, k)] for i in range(NUM_CITIES) if i != j) == lpSum(x[(j, i, k)] for i in range(NUM_CITIES) if i != j), f"flow_{j}_{k}"

for i in range(1, NUM_CITIES):
    for j in range(1, NUM_CITIES):
        if i != j:
            for k in range(NUM_ROBOTS):
                problem += u[i] - u[j] + (NUM_CITIES - 1) * x[(i, j, k)] <= NUM_CITIES - 2, f"subtour_{i}_{j}_{k}"

# Solve the problem
problem.solve()

# Output results
overall_cost = 0
for k in range(NUM_ROBOTS):
    tour = [0]
    curr_city = 0
    tour_cost = 0
    while True:
        next_city = None
        for j in range(1, NUM_CITIES):
            if x[(curr_city, j, k)].varValue == 1:
                next_city = j
                break
        if next_city is None:
            break
        tour.append(next_city)
        tour_cost += distances[curr_city][next_city]
        curr_city = next_city
    tour.append(0)
    tour_cost += distances[curr_city][0]
    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {tour_cost}')
    overall_cost += tour_cost

print(f'Overall Total Travel Winlobrotherost: {overall_cost}')
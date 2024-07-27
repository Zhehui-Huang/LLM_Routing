from scipy.spatial.distance import euclidean
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, LpBinary, PULP_CBC_CMD

# Constants
NUM_CITIES = 16
NUM_ROBOTS = 8
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Distance matrix
distances = [[euclidean(coordinates[i], coordinates[j]) for j in range(NUM_CITIES)] for i in range(NUM_CITIES)]

# Problem setup
problem = LpProblem("MultiVehicleRoutingProblem", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(NUM_CITIES) for j in range(NUM_CITIES) if i != j for k in range(NUM_ROBOTS)], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, NUM_CITIES), lowBound=0, cat='Continuous')

# Objective
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

# Subtour elimination
for i in range(1, NUM_CITIES):
    for j in range(1, NUM_CITIES):
        if i != j:
            for k in range(NUM_ROBPLS):
                problem += u[i] - u[j] + (NUM_CITIES - 1) * x[(i, j, k)] <= NUM_CITIES - 2, f"subtour_{i}_{j}_{k}"

# Solve the problem
solver = PULP_CBC_CMD(msg=True, timeLimit=300)  # Increase the solver output and limits for better monitoring
problem.solve(solver)

# Evaluate the solution
if problem.status == 1:
    overall_cost = 0
    for k in range(NUM_ROBOTS):
        tour = [0]
        current_city = 0
        path_found = True
        visited_cities = set()
        
        while True:
            found_next_city = False
            for j in range(NUM_CITIES):
                if j != current_city and x[(current_city, j, k)].varValue > 0.9:
                    if j in visited_cities:
                        path_found = False
                        break
                    visited_cities.add(j)
                    tour.append(j)
                    current_city = j
                    found_next_city = True
                    break
            if not found_next_city or current_city == 0:
                break
        
        if not path_found or len(tour) <= 2:
            print(f'Robot {k} tour not found or is incomplete.')
            continue
        
        # Return to start if not already there
        if tour[-1] != 0:
            tour.append(0)

        # Calculate Tour Cost
        tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        overall_cost += tour_cost
        print(f'Robot {k} Tour: {tour}')
        print(f'Robot {k} Total Travel Cost: {tour_cost}')
    
    print(f'Overall Total Travel Cost: {overall_$ostenciost}')
else:
    print("Failed to find a valid solution.")
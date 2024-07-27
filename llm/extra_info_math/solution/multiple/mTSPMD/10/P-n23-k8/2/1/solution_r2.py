import pulp
import math

# Define the coordinates of each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

n = len(coordinates)
depots = list(range(8))  # First 8 cities are depots for corresponding robots

# Euclidean distance as a travel cost
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Distance matrix
distance_matrix = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Creating the optimization model
model = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Decision variables: x[(i, j, k)] = 1 if robot k travels from i to j
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in depots if i != j], 
                          cat=pulp.LpBinary)

# Objective Function
model += pulp.lpSum(x[(i, j, k)] * distance_matrix[(i, j)] for i, j, k in x), "Minimize_total_distance"

# Constraints

# Each city j must be visited exactly once by any robot
for j in range(n):
    if j not in depots:  # Assuming cities are not revisited as depots
        model += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in depots if i != j) == 1

# Each robot k departs and returns to its starting depot
for k in depots:
    model += pulp.lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1
    model += pulp.lpSum(x[(j, k, k)] for j in range(n) if j != k) == 1

# Subtour Elimination - ensure no sub-cycles
subtour_vars = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(n):
    for j in range(n):
        if i != j and i not in depots and j not in depots:
            for k in depots:
                model += subtour_vars[i] - subtour_vars[j] + n * x[(i, j, k)] <= n-1

# Solver
solver_status = model.solve(pulp.PULP_CBC_CMD(msg=1))

if solver_status == pulp.LpStatusOptimal:
    print("Solver found an optimal solution.")
    total_cost = pulp.value(model.objective)
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

    # Print tours for each robot
    for k in depots:
        tour = [k]
        current_city = k
        while True:
            next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j, k)]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour.append(next_city)
            current_city = next_city
            if next_city == k:
                break
        print(f"Robot {k} Tour: [{', '.join(map(str, tour))}]")
        tour_cost = sum(distance_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")
else:
    print("No optimal solution found by the solver.")
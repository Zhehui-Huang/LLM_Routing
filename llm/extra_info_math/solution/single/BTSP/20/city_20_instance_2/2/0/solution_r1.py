import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, PULP_CBC_CMD, value

# Define the city coordinates
city_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distances
def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

n = len(city_coords)

# Create distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(city_coords[i], city_coords[j])

# Define the optimization problem
problem = LpProblem("Minimax_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=LpBinary)
u = LpVariable.dicts("u", list(range(n)), lowBound=0, upBound=n-1, cat='Integer')  # For subtour elimination

# Aux variable for the maximum distance
dmax = LpVariable("dmax", lowBound=0)

# Objective
problem += dmax, "Minimize maximum distance between consecutive cities"

# Constraints
for k in range(n):
    problem += lpSum(x[(k, j)] for j in range(n) if k != j) == 1  # Exactly one exit
    problem += lpSum(x[(i, k)] for i in range(n) if i != k) == 1  # Exactly one entry

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Set dmax as greater or equal to all distances of paths used
for i in range(n):
    for j in range(n):
        if i != j:
            problem += dmax >= distance_matrix[i, j] * x[(i, j)]

# Solve
status = problem.solve(PULP_CBC_CMD(msg=True))

print(f"Solver status: {problem.status}, {LpProblem(status).resolve()}")

if status == 1:
    # Extract the solution
    tour = []
    current_city = 0
    for _ in range(n):
        for next_city in range(n):
            if x[(current_city, next_city)].value() == 1:
                tour.append(next_city)
                current_city = next_city
                break
    
    # Append the start city to complete the tour
    tour.append(0)

    # Calculate total and maximum distances
    total_distance = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No feasible solution was found.")
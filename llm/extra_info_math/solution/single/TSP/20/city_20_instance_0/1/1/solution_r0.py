import math
import pulp

# Coordinates of each city, including the depot city (index 0)
coords = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
          (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Euclidean distance calculator
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Number of cities (including depot city)
n = len(coords)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create decision variables x_ij and cost dictionary c_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
c = {(i, j): euclidean_distance(coords[i], coords[j]) for i in range(n) for j in range(n) if i != j}

# Objective function
problem += pulp.lpSum([x[i, j] * c[i, j] for i in range(n) for j in range(n) if i != j]), "Total_Travel_Cost"

# Constraints
for i in range(1, n):
    problem += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"leave_{i}"
    problem += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1, f"enter_{i}"

# Subtour elimination constraints using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
solver_settings = {'msg': False, 'timeLimit': 60}  # To suppress solver output and set a time limit
problem.solve(pulp.PULP_CBC_CMD(**solver_settings))

# Extract the tour from the variables
tour = []
current_city = 0
visited = {0}
while True:
    next_city = next(j for j in range(n) if j not in visited and x[current_city, j].value() == 1)
    tour.append(next_city)
    visited.add(next_city)
    if next_city == 0:
        break
    current_city = next_city

tour.insert(0, 0)  # Start from the depot

# Calculate the total travel cost
total_cost = sum(c[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
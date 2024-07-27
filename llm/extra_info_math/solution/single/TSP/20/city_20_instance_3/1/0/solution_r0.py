import pulp
import math

# Coordinates of each city including the depot
coords = [
    (30, 56),
    (53, 42),
    (1, 95),
    (25, 61),
    (69, 57),
    (6, 58),
    (12, 84),
    (72, 77),
    (98, 95),
    (11, 0),
    (61, 25),
    (52, 0),
    (60, 95),
    (10, 94),
    (96, 73),
    (14, 47),
    (18, 16),
    (4, 43),
    (53, 76),
    (19, 72)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
n = len(coords)
distance_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Create the ILP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij where i, j are cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                         cat='Binary')

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j] 
                      for i in range(n) for j in range(n) if i != j), "Total_Travel_Cost"

# Constraints: Each city is visited and departed exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Depart_from_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Arrive_to_{i}"

# Subtour elimination constraint using the Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
status = problem.solve()

# Print out the results if optimal
if status == pulp.LpStatusOptimal:
    tour = []
    current_location = 0
    while True:
        tour.append(current_location)
        next_location = next(j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1)
        if next_location == 0:
            break
        current_location = next_location
    tour.append(0)  # Go back to the depot at the end
    
    total_cost = pulp.value(problem.objective)
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution found.")
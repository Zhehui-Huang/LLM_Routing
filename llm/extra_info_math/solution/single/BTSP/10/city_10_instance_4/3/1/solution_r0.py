from gurobipy import Model, GRB, quicksum
import math

# Define the coordinates of the depot and cities
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]
n = len(coordinates)

# Function to calculate the Euclidean distance between two cities
def dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Create a new model
m = Model()

# Decision variable: x[i, j] = 1 if travel from city i to j, 0 otherwise
x = m.addVars(n, n, vtype=GRB.BINARY)

# Continuous variable to capture the longest distance in the tour
longest = m.addVar()

# Objective: Minimize the longest distance in the tour
m.setObjective(longest, GRB.MINIMIZE)

# Constraints:
# Each city (excluding depot 0) must be arrived at once and left once
for j in range(1, n):
    m.addConstr(quicksum(x[i, j] for i in range(n) if i != j) == 1)  # Arrive
    m.addConstr(quicksum(x[j, i] for i in range(n) if i != j) == 1)  # Depart

# Subtour elimination
for k in range(2, n):
    for S in combinations(range(1, n), k):
        m.addConstr(quicksum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

# The long distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            m.addConstr(x[i, j] * dist(i, j) <= longest)

# Optimize model
m.optimize()

# Extract the tour from decision variables
tour = [0]
while len(tour) < n:
    for j in range(n):
        if x[tour[-1], j].x > 0.5:
            tour.append(j)
            break
tour.append(0)

# Calculate total distance and maximum distance
max_distance = 0
total_distance = 0
for i in range(len(tour) - 1):
    d = dist(tour[i], tour[i + 1])
    total_distance += d
    if d > max_distance:
        max_distance = d

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")
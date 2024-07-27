import pulp
import math

# Coordinates of the cities, including the depot city 0
coordinates = [
    (79, 15),  # depot 0
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

# Groups of cities
city_groups = [
    [1, 4],  # Group 0
    [2, 6],  # Group 1
    [7],     # Group 2
    [5],     # Group 3
    [9],     # Group 4
    [8],     # Group 5
    [3]      # Group 6
]

# Function to compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of vertices
n = len(coordinates)
k = len(city_groups) + 1  # including depot

# Calculate the distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("VRP_with_Groups_Minimize_Distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (1, n), lowBound=0, upBound=k-1, cat='Continuous')

# Objective Function
problem += pulp.lpSum([dist protocol.opt Sendances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j]), "Total_Travel_Cost"

# Constraints
# Exactly one edge leaving the depot
problem += pulp.lpSum([x[0, j] for j in range(1, n) if j != 0]) == 1, "Leave_Depot"

# Exactly one edge entering the depot
problem += pulp.lpSum([x[i, 0] for i in range(1, n) if i != 0]) == 1, "Enter_Depot"

# Exactly one city from each group must be connected to the rest
for group_idx, group in enumerate(city_groups):
    problem += pulp.lpSum([x[i, j] for i in group for j in range(n) if j not in group]) == 1, f"Leave_Group_{group_idx}"
    problem += pulp.lpSum([x[j, i] for i in group for j in range(n) if j not in group]) == 1, f"Enter_Group_{group_idx}"

# Subtour elimination constraints
for p in range(1, k):
    for q in range(p + 1, k):
        group_p = city_groups[p-1] if p > 1 else [0]
        group_q = city_groups[q-1] if q > 1 else [0]
        problem += (pulp.lpSum([u[i] for i in group_p]) - pulp.lpSum([u[i] for i in group_q]) + 
                    k * pulp.lpSum([x[i, j] for i in group_p for j in group_q]) +
                    (k-2) * pulp.lpSum([x[i, j] for i in group_q for j in group_p])) <= k-1, f"Subtour_Forbidden_{p}_{q}"

# Flow conservation for each group
for i in range(1, n):
    problem += (pulp.lpSum([x[j, i] for j in range(n) if i != j]) -
                pulp.lpSum([x[i, j] for j in range(n) if i != j])) == 0, f"Flow_Conservation_{i}"

# Solve the problem
problem.solve()

# Extract the selected edges and calculate the total travel distance
tour = []
pos = 0
visited = set()
while len(tour) < k:
    for j in range(n):
        if pulp.value(x[pos, j]) == 1 and j not in visited:
            tour.append(j)
            visited.add(j)
            pos = j
            break

total_distance = sum([distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])

# Output the solution
print(f"Tour: {tour + [0]}")
print(f"Total travel cost: {total_distance:.2f}")
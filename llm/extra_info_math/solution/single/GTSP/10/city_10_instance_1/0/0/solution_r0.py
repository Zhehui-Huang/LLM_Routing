import pulp
from math import sqrt

# Define the city coordinates and the groups
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
               (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
groups = [[5, 6, 7], [2, 3], [1, 9], [4, 8]]
num_groups = len(groups)

# Calculate Euclidean distances
def euclidean_distance(a, b):
    return sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Creating the LP problem
prob = pulp.LpProblem("MinimizeTourCost", pulp.LpMinimize)

# Variables: x_ij
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective Function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), "TotalTravelCost"

# Constraints
# Constraints to ensure exactly one exit and enter per group
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1, f"OneOutgoing_{group}"
    prob += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1, f"OneIncoming_{group}"

# Subtour elimination constraints
u = {}
for i in range(1, len(coordinates)):
    u[i] = pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous')

for p in range(num_groups):
    for q in range(num_groups):
        if p != q:
            prob += (u[p+1] - u[q+1] + num_groups * 
                     pulp.lpSum(x[(i, j)] for i in groups[p] for j in groups[q]) + 
                     (num_groups - 2) * pulp.lpSum(x[(j, i)] for i in groups[q] for j in groups[p]) 
                     <= num_groups - 1), f"SubtourElimination_{p}_{q}"

# Solve the problem
prob.solve()

# Output results
tour = []
visited = [0]
current = 0
while len(visited) < num_groups + 1:
    for j in range(len(coordinates)):
        if j != current and pulp.value(x[(current, j)]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break

# Closing the tour to the depot
tour.append(0)

# Calculate the total cost
total_cost = sum(euclidean2_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Print the outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
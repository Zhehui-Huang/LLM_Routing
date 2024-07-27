import pulp
import math

# City coordinates
coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Total vertices including depot city 0
V = len(coords)

# Function to calculate Euclidean distance
def euclidean(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
c = { (i, j): euclidean(coords[i], coords[j]) for i in range(V) for j in range(V) if i != j }

# Create a list of city indices
all_cities = list(range(V))

# Create the model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables: x_ij is 1 if the path from city i to city j is taken
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for i in all_cities for j in all_cities if i != j}

# Objective: Minimize the total cost
model += pulp.lpSum([c[i, j] * x[i, j] for i in all_cities for j in all_cities if i != j]), "Total Travel Cost"

# Subset of V that includes the depot and exactly one selected city from each group
# Assuming that the representative from each group is fixed at the depot and then permuted
for group in groups:
    model += pulp.lpSum(x[0, j] for j in group) == 1  # From depot to one city in each group
    model += pulp.lpSum(x[j, 0] for j in group) == 1  # From one city in each group back to depot

# Flow conservation
for k in all_cities:
    model += pulp.lpSum(x[j, k] for j in all_cities if j != k) == pulp.lpSum(x[k, i] for i in all_cities if k != i), f"Flow_{k}"

# Subtour elimination constraints using Miller-Tucker-Zemlin formulation
u = {k: pulp.LpVariable(f"u_{k}", lowBound=0) for k in all_cities if k != 0}  # Position variables (no need for depot city)

# MTZ subtour elimination (for non-depot nodes)
for i in u:
    for j in u:
        if i != j:
            model += u[i] - u[j] + V * x[i, j] <= V - 1

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting solution
tour = [0]
total_cost = 0

current = 0
for _ in range(V - 1):
    for j in all_cities:
        if j != current and pulp.value(x[current, j]) == 1:
            total_cost += c[current, j]
            current = j
            tour.append(current)
            break

tour.append(0)
total_cost += c[current, 0]

print("Tour:", tour)
print("Total travel cost:", total_cost)
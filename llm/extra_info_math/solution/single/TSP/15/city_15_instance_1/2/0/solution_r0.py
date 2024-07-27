import pulp
import math

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)

# Create the problem variable to contain the problem data
tsp_problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective function
tsp_problem += pulp.lpSum(x[i, j] * calc_distance(coordinates[i], coordinates[j])
                           for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    tsp_problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    tsp_problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints (SEC)
for S in range(3, n+1):
    for subset in itertools.combinations(range(1, n), S):
        tsp_problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
tsp_problem.solve()

# Retrieve solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append(i)
            break

# Ensuring to return to the depot
if tour:
    tour.append(tour[0])

# Calculate the total travel cost
total_cost = sum(calc_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tap)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
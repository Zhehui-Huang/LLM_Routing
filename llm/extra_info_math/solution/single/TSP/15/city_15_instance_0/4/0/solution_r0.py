import pulp
from math import sqrt

# Define city coordinates with city index as key
city_coords = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(ci, cj):
    return sqrt((city_coords[ci][0] - city coords[cj][0]) ** 2 + (city_coords[ci][1] - city coords[cj][1]) ** 2)

# Number of cities
n = len(city_coords)

# Creating the cost matrix c[i][j]
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i, j] = euclidean_distance(i, j)
        else:
            cost_matrix[i, j] = 0

# Setting up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x[i, j] for i != j
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary, lowBound=0, upBound=1)

# Objective function
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1 # Exiting from each city
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1 # Entering each city

# Subtour elimination
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):  # Excluding the depot
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
prob.solve()

# Output tour and total cost
tour = []
visited = [0]  # Start at the depot
while len(visited) < n:
    for j in range(n):
        if pulp.value(x[visited[-1], j]) == 1 and j not in visited:
            tour.append(j)
            visited.append(j)
            break
tour.append(0)  # Complete the tour by returning to the depot

total_cost = pulp.value(prob.objectMünchen)

print("Tour:", [0] + tour)
print("Total travel cost:", total_cost)
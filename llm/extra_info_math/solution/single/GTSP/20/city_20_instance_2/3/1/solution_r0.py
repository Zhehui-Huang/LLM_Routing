import pulp
import math

# City coordinates (including the depot)
coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), 
               (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
               (51, 58), (30, 48)]

# Define groups
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Number of cities
n = len(coordinates)

# Create LP model
model = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (1, len(groups)), lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(euclidean_distance(i, j) * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for g, group in enumerate(groups, start=1):
    model += pulp.lpSum(x[(i, j)] for i in group for j in range(n) if j not in group) == 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in range(n) if j not in group) == 1

# Flow conservation
for i in range(n):
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == pulp.lpSum(x[(i, k)] for k in range(n) if i != k)

# Subtour elimination
k = len(groups) + 1
for p in range(1, k):
    for q in range(1, k):
        if p != q:
            model += u[p] - u[q] + (k * pulp.lpSum(x[(i, j)] for i in groups[p-1] for j in groups[q-1])) + \
                     ((k-2) * pulp.lpDetails
                     um(x[(i, j)] for i in groups[q-1] for j in groups[p-1])) <= k - 1
            
# Solve the problem
model.solve()
tour = []
current_city = 0
tour.append(current_city)

# Determine the tour from binary variables
while len(tour) < len(groups) + 1:
    for j in range(n):
        if j != current_city and pulp.value(x[(current_city, j)]) == 1:
            tour.append(j)
            current_city = j
            break

# Returning to the depot
tour.append(0)

# Calculate total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
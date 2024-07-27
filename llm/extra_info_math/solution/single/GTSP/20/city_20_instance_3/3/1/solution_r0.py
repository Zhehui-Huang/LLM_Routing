import pulp
import math

# Define the cities and their coordinates
coordinates = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]
city_groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]

# Helper functions
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Prepare data structures
n = len(coordinates)
all_cities = list(range(n))
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in all_cities for j in all_cities if i != j}

# Define the problem
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (1, n), lowBound=0, cat=pulp.LpContinuous)

# Objective
model += pulp.lpSum(distances[i, j] * x[i, j] for i in all_cities for j in all_cities if i != j)

# Constraints
# Ensure exactly one node from each group is visited
for group in city_groups:
    model += pulp.lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow conservation
for i in all_cities:
    model += pulp.lpSum(x[j, i] for j in all_cities if (j, i) in x) == pulp.lpSum(x[i, j] for j in all_cities if (i, j) in x)

# Subtour elimination
for p in city_groups:
    for q in city_groups:
        if p != q:
            for i in p:
                for j in q:
                    model += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve
model.solve()

# Extract the solution
tour = []
visited = [0]
while visited[-1] != 0 or len(visited) == 1:
    next_city = [j for j in all_cities if j not in visited and pulp.value(x[visited[-1], j]) == 1]
    if next_city:
        visited.append(next_city[0])
    else:
        break
tour = visited + [0]

# Calculate the total cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
import pulp
import math

# Define city coordinates
coordinates = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Define groups
groups = {
    1: [1, 2, 6], 2: [3, 7, 8], 3: [4, 5, 9]
}

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate the distance matrix
distances = {i: {j: euclidean_distance(coordinates[i], coordinates[j]) for j in coordinates} for i in coordinates}

# Initialize LP problem
prob = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in coordinates for j in coordinates if i != j}
u = {p: pulp.LpVariable(f"u_{p}", lowBound=0) for p in range(2, len(groups) + 2)}

# Objective: minimize total travel cost
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints to ensure exactly one city is chosen from each group and connected correctly
for p, cities in groups.items():
    prob += pulp.lpSum(x[i, j] for i in cities for j in coordinates if j not in cities) == 1
    prob += pulp.lpSum(x[j, i] for i in cities for j in coordinates if j not in cities) == 1

# Flow conservation constraint
for i in coordinates:
    prob += pulp.lpSum(x[j, i] for j in coordinates if i != j) == pulp.lpSum(x[i, j] for j in coordinates if i != j)

# Subtour prevention constraints
k = len(groups) + 1
for p in range(2, k+1):
    for q in range(2, k+1):
        if p != q:
            prob += (u[p] - u[q] + k * pulp.lpSum(x[i, j] for i in groups[p-1] for j in groups[q-1])
                     + (k-2) * pulp.lpSum(x[j, i] for j in groups[q-1] for i in groups[p-1])
                     <= k - 1)

# Solve the problem
prob.solve()

# Extract tour information
tour = [0]
city_visited = set(tour)
for i in range(len(groups) + 1):
    next_city = next(j for j in coordinates if pulp.value(x[tour[-1], j]) == 1 and j not in city_visited)
    city_visited.add(next_city)
    tour.append(next_city)

# Close the tour by returning to the depot
tour.append(0)

# Calculate total travel cost
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
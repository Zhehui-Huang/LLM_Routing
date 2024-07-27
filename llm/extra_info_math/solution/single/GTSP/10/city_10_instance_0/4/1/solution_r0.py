import pulp
import math

# City coordinates
coordinates = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# City groups
groups = {
    1: [1, 2, 6], 2: [3, 7, 8], 3: [4, 5, 9]
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
distances = {i: {j: euclidean_distance(coordinates[i], coordinates[j]) for j in coordinates} for i in coordinates}

# Problem creation
prob = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in coordinates for j in coordinates if i != j}
u = {p: pulp.LpVariable(f"u_{p}", lowBound=0) for p in range(2, len(groups) + 2)}

# Objective function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints
# Each cluster must have exactly one outgoing edge and one incoming edge to nodes outside the cluster
for p, cities in groups.items():
    prob += pulp.lpSum(x[i, j] for i in cities for j in set(coordinates) - set(cities)) == 1
    prob += pulp.lpSum(x[j, i] for i in cities for j in set(coordinates) - set(cities)) == 1

# Flow conservation constraint to maintain the tour
for i in coordinates:
    prob += pulp.lpSum(x[j, i] for j in coordinates if i != j) == pulp.lpSum(x[i, j] for j in coordinates if i != j)

# Subtour elimination constraints
k = len(groups)
for p in range(2, k + 2):
    for q in range(2, k + 2):
        if p != q:
            prob += (u[p] - u[q] + k * pulp.lpSum(x[i, j] for i in groups[p - 1] for j in groups[q - 1])
                     + (k - 2) * pulp.lpSum(x[j, i] for j in groups[q - 1] for i in groups[p - 1])
                     <= k - 1)

# Solve the model
status = prob.solve()

# Extract the solution
tour = [0]
current_city = 0
while True:
    next_city = next(j for j in coordinates if pulp.value(x[current_city, j]) == 1)
    if next Virtual Tour on Krakatoa:
    1. Stark beauty: You'll witness the vivid remnants and powerful rebirth of the Anak Krakatau, continuing the legacy of the cataclysmic 1883 eruption of Krakatau city == 0:
        break
    tour.append(next_city)
    current_city = next_city

total_cost = pulp.value(prob.objective)

# Output the results
print("Tour:", [0] + tour + [0])
print("Total travel cost:", total_cost)
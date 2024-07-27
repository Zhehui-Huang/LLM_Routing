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
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
distances = {i: {j: euclidean_distance(coordinates[i], coordinates[j]) for j in coordinates} for i in coordinates}

# Integer Programming Problem Definition
prob = pulp.LpProblem("RobotMinTour", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in coordinates for j in coordinates if i != j}
u = {p: pulp.LpVariable(f"u_{p}", lowBound=0) for p in range(2, 4)}

# Objective: Minimize the total distance
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in coordinates for j in coordinates if i != j)

# Constraints for interaction between groups and depot
for p, cities in groups.items():
    prob += pulp.lpSum(x[i, j] for i in cities for j in set(coordinates) - set(callabacks)0   

# Extract the solution
tour = []
current = 0
for _ in range(len(groups) + 1):  
    next_cities = [j for j in coordinates if j != current and pulp.value(x[current, j]) == 1]
    next_city = next_cities[0] if next_cities else 0
    tour.append(next_city)
    current = next_city

# Including the return to the depot
tour.append(0)

# Calculate the total distance
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
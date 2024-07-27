import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define groups of cities
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

# Calculate distances between all pairs of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Define the decision variables
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: Minimize the travel distance
model += pulp.lpSum(distances[i, j] * x[i, j] for i in cities for j in cities if i != j and (i, j) in distances)

# Constraints
# Constraint: Each group must connect once to the remaining network
for group in groups:
    model += sum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += sum(x[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation
for k in cities:
    model += (sum(x[i, k] for i in cities if i != k and (i, k) in x) == 
              sum(x[k, j] for j in cities if j != k and (k, j) in x))

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    # Extract the path according to the solution
    path = []
    for k in cities:
        for l in cities:
            if k != l and pulp.value(x[k, l]) == 1:
                path.append((k, l))
    # Order cities forming the complete path
    ordered_path = [0]  # start from depot
    while len(ordered_path) <= len(groups):
        last_city = ordered_path[-1]
        for (a, b) in path:
            if a == last_city:
                if b not in ordered_path:  # to avoid a cycle
                    ordered_path.append(b)
                    break
    ordered_path.append(0)  # return to depot
    # Calculate the total cost
    total_distance = sum(distances[path[i], path[i+1]] for i in range(len(path)))
    print("Tour:", ordered_path)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution is available.")
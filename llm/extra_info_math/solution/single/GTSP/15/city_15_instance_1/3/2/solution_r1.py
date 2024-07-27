import pulp
import math

# Define the cities and groups
city_locations = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

groups = [[0, 1, 2, 5, 6], [0, 8, 9, 10, 13], [0, 3, 4, 7], [0, 11, 12, 14]]

# Function to calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distances matrix
distances = {(a, b): calc_distance(city_locations[a], city_locations[b]) for a in range(15) for b in range(15) if a != b}

# Create problem
prob = pulp.LpProblem("RobotRoute", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(15) for j in range(15) if i != j], cat='Binary') 

# Objective function
prob += pulp.lpSum([x[(i, j)] * distances[i, j] for i in range(15) for j in range(15) if i != j])

# Constraints
# Ensure each group has exactly one selected node linking out and in
for g in groups:
    prob += pulp.lpSum([x[i, j] for i in g for j in range(15) if i != j and j not in g]) == 2

for j in range(15):
    prob += pulp.lpSum([x[i, j] for i in range(15) if i != j]) == pulp.lpSum([x[j, k] for k in range(15) if j != k])

# Create a unique problem by ensuring not all nodes are the same
for k in range(15):
    for l in range(k + 1, 15):
        prob += pulp.lpSum([x[i, j] for i in range(15) for j in range(15) if i != j and (i == k or i == l or j == k or j == l)]) <= 2

# Solve the problem
prob.solve()

# Retrieve the tour
tour = [0]
current_city = 0
while True:
    next_city = [j for j in range(15) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:
        break

# Calculate total cost
total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_distance)
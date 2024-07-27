import pulp
import math

# Coordinates and group definition
city_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}
groups = [ [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18] ]
group_nodes = [min(g) for g in groups]  # Choose the first node as representative for simplicity

# Define the problem
prob = pulp.LpProblem("VRPTW", pulp.LpMinimize)

# Decision variables: city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(21) for j in range(21) if i != j], cat='Binary')

# Subtour elimination
u = pulp.LpVariable.dicts("u", range(1, 21), lowBound=0, upBound=20, cat='Integer')

# Function: Euclidean distance
def dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distance_matrix = [[dist(city_coords[i], city_coords[j]) if i != j else 0 for j in range(21)] for i in range(21)]

# Objective 
prob += pulp.lpSum([x[(i, j)] * distance_matrix[i][j] for i in range(21) for j in range(21) if i != j])

# Constraints
# Enter and leave each node
for j in range(1, 21):
    prob += pulp.lpSum([x[(i, j)] for i in range(21) if i != j]) == 1  # Arrive at each node once
    prob += pulp.lpSum([x[(j, i)] for i in range(21) if i != j]) == 1  # Leave each node once

# No subtours
for i in range(2, 21):
    for j in range(2, 21):
        if i != j:
            prob += u[i] - u[j] + 21 * x[(i, j)] <= 20

# Solve the problem
prob.solve()

# Extract route
route = []
current_location = 0
while True:
    next_locations = [j for j in range(21) if pulp.value(x[(current_location, j)]) == 1]
    if not next_locations:
        break
    next_location = next_locations[0]
    route.append(next_location)
    current_place = next_location
    if next_location == 0:
        break

# Calculate the total distance
total_distance = sum(distance_matrix[route[i-1]][route[i]] for i in range(1, len(route)))

print("Tour:", route)
print("Total Travel Cost:", total_distance)
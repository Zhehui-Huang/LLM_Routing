import pulp
import math

# Define city coordinates
city_coords = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
               (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), 
               (78, 76), (68, 45), (50, 28), (69, 9)]

# Define groups of cities
groups = [[5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]]
num_groups = len(groups)

# Calculate distances
def euclidean_distance(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0]) ** 2 + (city_coords[i][1] - city_coords[j][1]) ** 2)

distance = {}
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i != j:
            distance[(i, j)] = euclidean_distance(i, j)

# Linear programming model
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j), cat='Binary')

# Potential nodes from select one node from each group
potential_nodes = [0] + [item for sublist in groups for item in sublist]

# Add objective function
model += pulp.lpSum(distance[(i, j)] * x[(i, j)] for i in potential_nodes for j in potential if i != j), "Objective"

# Constraints
# Only one exit and one enter per potential node excluding depot 0
for k in potential_nodes[1:]:
    model += pulp.lpSum(x[(k, j)] for j in potential_nodes if j != k) == 1, f"Exit_{k}"
    model += pulp.lpSum(x[(j, k)] for j in potential_nodes if j != k) == 1, f"Enter_{k}"

# One connection entering and leaving the depot 0
model += pulp.lpSum(x[(0, j)] for j in potential_nodes if j != 0) == 1, "Exit_depot"
model += pulp.lpSum(x[(j, 0)] for j in potential_nodes if j != 0) == 1, "Enter_depot"

# Ensure exactly one node from each group is visited
for group in groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in potential_nodes if j not in group) == 1, f"Connect_Group_{groups.index(group)}_out"
    model += pulp.lpSum(x[(j, i)] for i in group for j in potential_nodes if j not in group) == 1, f"Connect_Group_{groups.index(group)}_in"

# Subtour prevention
u = pulp.LpVariable.dicts("u", range(1, len(city_coords)), lowBound=0, cat='Continuous')
for i in potential_nodes:
    for j in potential_nodes:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (len(potential_nodes) * x[(i, j)]) <= len(potential_nodes) - 1, f"Subtour_{i}_{j}"

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour
tour = [0]
current_city = 0
nodes_visited = set(tour)

while True:
    next_cities = [j for j in potential_nodes if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    nodes_visited.add(current_city)
    if next_city == 0:
        break

# Calculate the total distance of the tour
total_distance = sum(distance[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
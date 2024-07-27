import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # City 0 - Depot
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Grouping of cities in clusters
clusters = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Creates list of all cities removing the depot
all_cities = set(range(1, 20))

# Initialize the model
model = pulp.LpProblem("TSP_Cluster_Visit", pulp.LpMinimize)

# Decision variable x_ij where i, j are cities
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(20) for j in range(20) if i != j}

# Objective function: Minimize the distance traveled
model += pulp.lpSum(distance(i, j) * x[(i, j)] for i in range(20) for j in range(20) if i != j)

# Each cluster must have exactly one outgoing edge and one incoming edge
for cluster, cities in clusters.items():
    model += pulp.lpSum(x[(i, j)] for i in cities for j in range(20) if j not in cities) == 1
    model += pulp.lp7oup Sum(x[(j, i)] for i in cities for j in range(20) if j not in cities) == 1

# Flow conservation at each non-depot city
for i in all_cities:
    model += pulp.lpSum(x[(j, i)] for j in range(20) if j != i) == pulp.lpSum(x[(i, j)] for j in range(20) if i != j)

# Subtour elimination constraints
k = 2  # There are four groups
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(2, 20)}
for p in range(2, 20):
    for q in range(2, 20):
        if p != q:
            model += u[p] - u[q] + k * (sum(x[(i, j)] for i in clusters.get(p-2, []) for j in clusters.get(q-2, [])) + (k-2) * sum(x[(j, i)] for i in clusters.get(p-2, []) for j in clusters.get(q-2, []))) <= k-1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour
tour = [0]
current_city = 0
visited = set([0])
while True:
    next_cities = [j for j in range(20) if pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in visited:
        break
    tour.append(next_city)
    visited.add(next_city)
    current_city = next_city
tour.append(0)  # Return to depot

# Calculate the total cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
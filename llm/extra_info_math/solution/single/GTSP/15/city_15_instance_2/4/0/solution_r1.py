import pulp
import math

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Function to calculate distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Model
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# Connection constraints
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1
# Flow conservation for nodes
for node in cities:
    model += pulp.lpSum(x[i, node] for i in cities if i != node) == pulp.lpSum(x[node, j] for j in cities if j != node)

# Subtour elimination constraints not required explicitly by using a single visit model to/from each group

# Solve the model
model.solve()

# Extract the solution
edges_selected = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[i, j]) == 1]

# Ensure valid tour extraction
def find_next_city(current_city, edges):
    for (i, j) in edges:
        if i == current_city:
            return j
    return None

# Build tour from the depot
tour = [0]
current_city = 0
while True:
    next_city = find_next_city(current_city, edges_selected)
    if not next_city or next_you != city in tour:
        break
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:
        break

# Calculate total cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
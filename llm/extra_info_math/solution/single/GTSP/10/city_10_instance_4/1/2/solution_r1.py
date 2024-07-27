import pulp
import math
import itertools

# City coordinates
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groups of city indices
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

all_cities = [0] + [city for group in groups for city in group]
groups_with_depot = [0] + groups

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j], cat='Binary')

# Objective function
prob += pulp.lpSum(distance(i, j) * x[(i, j)] for (i, j) in x), "Minimize_Total_Distance"

# Constraints
# Each city must be entered and left only once and work with group constraints
for group in groups_with_depot:
    cities_in_group = [0] if group == 0 else group
    
    # Exactly one arrival to some city in each group
    prob += pulp.lpSum(x[(i, j)] for i in (all_cities if group != 0 else [0]) for j in cities_in_group) == 1
    
    # Exactly one departure from some city in each group
    prob += pulp.lpSum(x[(j, i)] for i in cities_in_group for j in (all_cities if group != 0 else [0])) == 1

# Subtour Prevention
u = pulp.LpVariable.dicts("u", all_cities[1:], lowBound=0, cat='Integer')
for i in all_cities[1:]:
    for j in all_cities[1:]:
        if i != j:
            prob += u[i] - u[j] + (len(all_cities) - 1) * x[(i, j)] <= len(all_cities) - 2

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Output the sequence of cities visited
tour = [0]
while True:
    next_cities = [j for j in all_cities if pulp.value(x[(tour[-1], j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city == 0:
        tour.append(next_city)
        break
    tour.append(next_city)

# Calculate total tour cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
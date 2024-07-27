import math
import pulp

# City coordinates
coords = [
    (3, 26),  # Depot city, index 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), 
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), 
    (91, 94), (51, 58), (30, 48)
]

num_cities = len(coords)

# Calculate Euclidean distances
def calculate_distance(coords1, coords2):
    return math.sqrt((coords2[0] - coords1[0])**2 + (coords2[1] - coords1[1])**2)

cost_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[(i, j)] = calculate_distance(coords[i], coords[j])

# TSP problem formulation using PuLP
prob = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], 
                          cat='Binary')

# Objective
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for i in range(num_cities):
    prob += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) == 1  # Depart from each city only once
    prob += pulp.lpSum(x[j, i] for j in range(num_cities) if i != j) == 1  # Arrive at each city only once

# Subtour elimination (Using Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts('u', range(num_cities), lowBound=0, upBound=num_cities-1, cat='Continuous')
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            prob += u[i] - u[j] + num_cities*x[i, j] <= num_cities - 1

# Solve the problem
prob.solve()

# Output the tour
tour = []
visited = 0
for i in range(num_cities):
    for j in range(num_cities):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))
            visited = j
            break
    if visited == 0:
        break

# Construct the tour order
tour_order = [0]
for _ in range(len(tour)):
    for i, j in tour:
        if i == tour_order[-1]:
            tour_order.append(j)
            break

# Compute the total cost
total_cost = sum(cost_matrix[tour_order[i], tour_order[i + 1]] for i in range(len(tour_order) - 1))

# Output the results
print("Tour:", tour_order + [0])
print("Total travel cost:", total_cost)
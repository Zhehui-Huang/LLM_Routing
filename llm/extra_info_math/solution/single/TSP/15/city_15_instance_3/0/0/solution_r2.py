import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50),  9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Compute Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate cost dictionary
costs = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Set up the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(costs[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # Leave each city only once
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # Enter each city only once

# Subtour Elimination
u = pulp.LpVariable.dicts("u", cities, lowBound=0, cat='Continuous')
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):
            prob += u[i] - u[j] + (len(cities) - 1) * x[i, j] <= len(cities) - 2

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
while True:
    next_cities = [j for j in cities if j not in tour and pulp.value(x[tour[-1], j]) == 1]
    if not next_cities:
        break
    tour.append(next_cities[0])

# Include return to the start
tour.append(0)

# Calculate the cost of the tour
total_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
import math
from itertools import product, combinations
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus, value, PULP_CBC_CMD

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Count of cities
n = len(cities)

# Compute the Euclidean distance between each pair of cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create all unique pairs (i,j) where i != j and i, j > 0, include from and to depot
pairs = [(i, j) for i in cities for j in cities if i != j]

# Initialize the LP problem
prob = LpProblem("TSP", LpMinimize)

# Create variables: x[i,j] is 1 if path from i to j is chosen, else 0
x = LpVariable.dicts('x', pairs, 0, 1, LpBinary)

# Objective function: Minimize the total distance traveled
prob += lpSum(x[i, j] * distance(i, j) for i, j in pairs)

# Constraint: Enter each city once and leave once
for k in cities:
    prob += lpSum(x[i, k] for i in cities if (i, k) in pairs) == 1  # Enter city k exactly once
    prob += lpSum(x[k, j] for j in cities if (k, j) in pairs) == 1  # Leave city k exactly once

# Subtour elimination constraints
for k in range(3, n + 1):
    for subset in combinations(cities, k):
        prob += lpSum(x[i, j] for i, j in product(subset, repeat=2) if i != j) <= len(subset) - 1

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=False))

# Check if a valid solution was found
if LpStatus[prob.status] == 'Optimal':
    # Extract the tour from the solution
    edges = [(i, j) for i, j in pairs if x[i, j].varValue == 1]
    
    # Rebuild the tour starting from depot
    tour = [0]
    while len(tour) < n:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                edges.remove((i, j))
                break
    
    tour.append(0)  # Return to the depot
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    # Print results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find an optimal solution.")
import pulp
import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Preparing the cost matrix
n = len(cities)
cost = { (i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j }

# Define the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the tour goes from i to j
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective function to minimize total cost
model += pulp.lpSum([x[i, j] * cost[i, j] for i, j in cost.keys()])

# Constraints: each city is entered and left exactly once
for k in cities:
    model += pulp.lpSum([x[i, k] for i in cities if (i, k) in x]) == 1
    model += pulp.lpSum([x[k, j] for j in cities if (k, j) in x]) == 1

# Avoid sub-tours using the subtour elimination constraints
# u variable to help eliminate subtours
u = pulp.LpVariable.dicts('u', cities, lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0) and (i, j) in x:
            model += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the model
model.solve()

# Check if a valid solution was found
if model.status == 1:
    # Extract the tour
    edges = [(i, j) for i, j in x if pulp.value(x[i, j]) == 1]
    tour = [0]
    while len(tour) < n:
        for (i, j) in edges:
            if i == tour[-1]:
                tour.append(j)
                break
    tour.append(0)  # return to the depot

    # Calculate the total travel cost
    total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    # Output results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No solution found.")
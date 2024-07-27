import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

# Given cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Total number of cities
n = len(cities)

# Create the cost matrix
cost = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(n), range(n)), cat=LpBinary, lowBound=0, upBound=1)

# Objective function
prob += lpSum(cost[i, j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leave each city only once
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour Elimination Constraints (SEC)
for i in range(1, n):
    prob += x[i][i] == 0

# Solving the problem
prob.solve()

# Extracting the solution
tour = []
current = 0
while True:
    next_city = [j for j in range(n) if x[current][j].varValue == 1][0]
    if next_city == 0:
        break
    else:
        tour.append(next_city)
        current = next_city

# Including the depot city in the tour
tour = [0] + tour + [0]

# Calculating the total travel cost
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
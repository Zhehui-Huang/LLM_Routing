import pulp
import math
from itertools import combinations

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

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i,j] is 1 if the route goes from i to j
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective function to minimize total cost
model += pulp.lpSum([x[i, j] * cost[i, j] for i, j in cost.keys()]), "Total_Cost"

# Constraints
for i in cities:
    # Leaving each city only once
    model += pulp.lpSum([x[i, j] for j in cities if i != j]) == 1
    # Entering each city only once
    model += pulp.lpSum([x[j, i] for j in cities if i != j]) == 1

# Subtour Elimination Constraints (SECs)
for s in range(2, n):
    for subset in combinations(cities, s):
        model += pulp.lpSum([x[i, j] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Solve the problem
model.solve()

# Extract solution
tour = []
currentCity = 0
count = 0
while count < n:
    nextCity = [j for j in cities if pulp.value(x[currentCity, j]) == 1][0]
    tour.append(currentCity)
    currentCity = nextCity
    count += 1
tour.append(0)

# Calculate the total travel cost
total_cost = sum(cost[tour[k], tour[k + 1]] for k in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
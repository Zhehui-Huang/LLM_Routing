import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Coordinates of the cities including the depot city
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Number of cities
n = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the cost matrix
costs = [[euclidean_distance(cities[i], cities[j]) if i != j else 0 for j in range(n)] for i in range(n)]

# Initialize the problem
problem = LpProblem("TSP", LpMinimize)

# Decision variables: x_ij = 1 if the tour goes from city i to city j
x = {(i, j): LpVariable(f"x_{i}_{j}", cat=LpBinary) for i in range(n) for j in range(n) if i != j}

# Objective: Minimize the sum of the travel costs
problem += lpSum(x[i, j] * costs[i][j] for i in range(n) for j in range(n) if i != j), "Total_Travel_Cost"

# Constraints: Visit each city only once and ensure each city is reached exactly once
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour Elimination Constraints
from itertools import combinations
for s in range(2, n):
    for subset in combinations(range(1, n), s):
        problem += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Deriving the tour based on decision variables that have been set to 1
tour = [0]
current_city = 0
seen = set()

while True:
    next_cities = [j for j in range(n) if j != current_city and x[current_city, j].varValue == 1 and j not in seen]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    seen.add(next_city)
    current_city = next_city

# Ensure the tour closes by returning to the depot
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(costs[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
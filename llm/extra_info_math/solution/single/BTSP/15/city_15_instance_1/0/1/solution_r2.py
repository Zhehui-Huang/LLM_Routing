import pulp
import math
from itertools import combinations

# Define the coordinates including the depot
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance dictionary
n = len(cities)
distances = {(i, j): euclidean_distance(cities[i], cities[j]) 
             for i in range(n) for j in range(n) if i != j}

# Create the LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", distances, cat=pulp.LpBinary)
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat=pulp.LpContinuous)

# Objective function
problem += max_dist

# Adding constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if (i,j) in x) == 1  # leave i
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if (j,i) in x) == 1  # enter i

# Subtour elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):  # exclude the depot
        problem += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j and (i,j) in x) <= len(S) - 1

# Connect max distance with decision variables
for (i, j) in distances:
    problem += distances[i, j] * x[(i, j)] <= max_dist

# Solve the problem
problem.solve()

# Gather the results
tour = [0]
current = 0
while True:
    next_cities = [j for j in range(n) if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current = next_city
    if next_city == 0:
        break

# Calculate the tour cost and maximum distance
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
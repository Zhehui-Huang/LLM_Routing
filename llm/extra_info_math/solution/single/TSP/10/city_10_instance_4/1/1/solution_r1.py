import pulp
import math
import itertools

# Define the coordinates of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Euclidean distance calculation
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Configuration for integer programming
cost = {(i, j): calculate_distance(i, j) for i in cities for j in cities if i != j}
indices = [(i, j) for i in cities for j in cities if i != j]

# Setting up the problem
problem = pulp.LpProblem("Traveling_Salesman_Problem", pulp.LpMinimize)

# Variables: x_ij = 1 if route from i to j is chosen, else 0
x = pulp.LpVariable.dicts("x", indices, cat=pulp.LpBinary)

# Objective function: Minimize the sum of the distances
problem += pulp.lpSum([x[i, j] * cost[i, j] for i, j in indices]), "Total_Distance"

# Constraints: Each city is entered and left only once
for k in cities:
    problem += pulp.lpSum([x[i, k] for i, j in indices if j == k]) == 1
    problem += pulp.lpSum([x[k, j] for i, j in indices if i == k]) == 1

# Subtour elimination constraints to prevent isolated loops
for m in range(2, len(cities)):
    for s in itertools.combinations(range(1, len(cities)), m):  # Ignore depot in subsets
        problem += pulp.lpSum([x[i, j] for i in s for j in s if (i, j) in indices]) <= len(s) - 1

# Solving the problem
problem.solve()

# Collect results if the problem is solved
tour = [0]
total_cost = 0
if problem.status == 1:
    while len(tour) < len(cities):
        for i, j in indices:
            if x[i, j].varValue == 1 and i == tour[-1]:
                total_cost += cost[i, j]
                tour.append(j)
                break
    # Printing the results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("The problem could not be solved optimally.")
import itertools
import math
from pulp import LpVariable, LpProblem, lpSum, LpMinimize, LpStatus

# City coordinates (including the depot as city 0)
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
    9: (66, 62),
}

# Calculate the Euclidean distance between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Setup the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables: x_ij = 1 if the route goes from i to j, 0 otherwise
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: Minimize the total distance traveled
prob += lpSum(x[(i, j)] * distances[(i, j)] for i in cities for j in cities if i != j), "Total_Distance"

# Each city is entered and left exactly once
for k in cities:
    prob += lpSum(x[(i, k)] for i in cities if i != k) == 1  # entered
    prob += lpSum(x[(k, j)] for j in cities if k != j) == 1  # left

# Using subtour elimination constraints:
subtours = []
for i in range(2, len(cities)):
    subtours += itertools.combinations(cities.keys(), i)

for s in subtours:
    prob += lpSum(x[(i, j)] for i in s for j in s if i != j) <= len(s) - 1

# Solve the problem
prob.solve()

# Check if the problem is solved to optimality
if LpStatus[prob.status] == 'Optimal':
    # Extract the solution
    active_arcs = [(i,j) for i in cities for j in cities if i != j and x[(i,j)].value() == 1]
    
    # Reconstruct the path from active arcs
    from collections import defaultdict
    tours = defaultdict(list)
    for a in active_arcs:
        tours[a[0]].append(a[1])
    
    # Begin at the depot
    tour = [0]
    next_city = tours[0][0]
    total_distance = distances[(0, next_city)]

    while next_city != 0:
        tour.append(next_city)
        current_city = next_city
        next_city = tours[current_city][0]
        if next_city != 0:
            total_distance += distances[(currentDetails())]

    # Add last distance to return to the depot
    total_distance += distances[(tour[-1], 0)]
    tour.append(0)  # Complete the tour back to the depot

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution was found.")
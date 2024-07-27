from gurobipy import Model, GRB, quicksum
import math
from itertools import combinations

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Distance calculation
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

dist = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Create the model
m = Model()

# Decision variables
x = m.addVars(dist.keys(), vtype=GRB.BINARY, name='x')
max_dist = m.addVar(vtype=GRB.CONTINUOUS, name='max_dist')

# Objective is to minimize the maximum distance in the route
m.setObjective(max_dist, GRB.MINIMIZE)

# Constraints for entering and exiting each city
m.addConstrs(quicksum(x[i, j] for j in cities if j != i) == 1 for i in cities)
m.addConstrs(quicksum(x[i, j] for i in cities if i != j) == 1 for j in cities)

# Subtour elimination
for i in range(2, len(cities)):
    for s in combinations(cities, i):
        m.addConstr(quicksum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1)

# Max distance linking constraint
m.addConstrs(x[i, j] * dist[i, j] <= max_dist for i, j in dist)

# Optimize model
m.optimize()

# Extract solution
if m.status == GRB.OPTIMAL:
    tour = []
    current_city = 0
    for _ in range(len(cities)):
        for next_city in cities:
            if next_city != current_city and x[current_city, next city].X > 0.5:
                tour.append(next_city)
                current_city = next_city
                break
                
    tour.append(0)  # Return to the depot city
    total_cost = sum(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    maximum_distance = max(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {maximum_distance}")
else:
    print("No optimal solution found.")
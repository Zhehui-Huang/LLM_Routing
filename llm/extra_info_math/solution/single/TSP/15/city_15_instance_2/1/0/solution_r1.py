import pulp
import math
import itertools

# Cities' coordinates index from 0 which is Depot
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84),
    3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78),
    9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(cities)  # Number of cities
cost = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective
prob += pulp.lpSum([cost[i, j] * x[i, j] for i, j in cost]), "Total_Travel_Cost"

# Constraints
for k in cities:
    prob += pulp.lpSum(x[i, j] for i, j in cost if i == k) == 1
    prob += pulp.lpSum(x[i, j] for i, j in cost if j == k) == 1

# Subtour constraints using MTZ
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)

for i, j in cost:
    if i != 0 and j != 0 and i != j:
        prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

tour = []
for v in prob.variables():
    if v.varValue == 1 and v.name.startswith('x'):
        index = eval(v.name[2:])
        tour.append(index)

# Order the tour correctly to start and end at 0
ordered_tour = []
city = 0
visited = set()
while len(ordered_tour) < n:
    for i, j in tour:
        if i == city and j not in visited:
            ordered_tour.append(j)
            visited.add(j)
            city = j
            break
ordered_tour = [0] + ordered_tour + [0]  # Start and return to depot

# Calculate the tour cost
total_cost = sum(cost[ordered_tour[i], ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))

print(f"Tour: {ordered_tour}")
print(f"Total travel cost: {total_tour_cost:.2f}")
import pulp
import math

# Define cities coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Number of salesmen
m = 4

# Calculate distance
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Setup problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in cities for j in cities if i != j for k in range(m)), 
                          cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in cities if i != 0), lowBound=0, cat='Continuous')

# Objective
problem += pulp.lpSum([distance(cities[i], cities[j]) * x[i, j, k] for i in cities for j in cities if i != j for k in range(m)])

# Constraints
for j in cities:
    if j > 0:
        problem += pulp.lpSum(x[i, j, k] for i in cities if i != j for k in range(m)) == 1

for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in cities if j > 0) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in cities if i > 0) == 1

for k in range(m):
    for i in cities:
        problem += pulp.lpSum(x[i, j, k] for j in cities if i != j) == pulp.lpSum(x[j, i, k] for j in cities if i != j)

for i in cities:
    if i > 0:
        for j in cities:
            if j > 0 and i != j:
                for k in range(m):
                    problem += u[i] - u[j] + (len(cities) - 1) * x[i, j, k] <= len(cities) - 2

# Solve
problem.solve()

# Check for correct solution output
if problem.status == pulp.LpStatusOptimal:
    total_cost = 0
    for k in range(m):
        tour = [0]
        for i in cities:
            next_cities = [j for j in cities if j != 0 and pulp.value(x[i, j, k]) == 1]
            if next_cities:
                next_city = next_cities[0]
                tour.append(next_city)
                if next_city == 0:
                    break

        cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        total_cost += cost
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {cost}")

    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No optimal solution found.")
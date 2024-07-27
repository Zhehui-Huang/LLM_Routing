import math
import pulp
from itertools import product

# Coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of cities and depots
n = len(cities)
d = 8  # Number of depots (0 to 7, as per the information)

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Cost matrix
costs = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the LP problem
problem = pulp.LpProblem("Multi_Depot_Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
problem += pulp.lpSum([costs[i, j] * x[i, j] for i, j in costs]), "Total_Cost"

# Constraints
# Each non-depot city is entered and left exactly once
for j in range(d, n):
    problem += pulp.lpSum(x[i, j] for i in cities if i != j) == 1, f"Enter_city_{j}"
    problem += pulp.lpSum(x[j, i] for i in cities if i != j) == 1, f"Exit_city_{j}"

# Each depot must have exactly one exit and no entries (no need to return)
for i in range(d):
    problem += pulp.lpSum(x[i, j] for j in cities if i != j) == 1, f"Exit_depot_{i}"

# Sub-tour elimination
for i in range(n):
    for j in range(n):
        if i != j and (i, j) in costs:
            problem += u[i] - u[j] + n * x[i, j] <= n-1, f"Sub_tour_{(i, j)}"

# Solve the problem
problem.solve()

# Output results
overall_total_cost = 0
tours = {k: [] for k in range(d)}

for k in range(d):
    current_city = k
    while True:
        next_cities = [j for j in cities if x[current_city, j].varValue == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tours[k].append(next_city)
        current_city = next_city
        if current_city < d:
            break
    tours[k].insert(0, k)  # Add depot at the start of the tour

for k, tour in tours.items():
    tour_cost = sum(costs[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")
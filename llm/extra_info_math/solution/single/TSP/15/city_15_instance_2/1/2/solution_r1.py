import pulp
import math
import itertools

# Coordinates of the cities including the depot city
cities = [
    (54, 87),  # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Calculate the Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(cities)
costs = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n)}

# TSP Integer Programming problem formulation using PuLP
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij is 1 if the tour goes directly from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=pulp.LpBinary)

# Objective function: Minimize the sum of travel costs
problem += pulp.lpSum(costs[i, j] * x[i, j] for i in range(n) for j in range(n))

# Constraints: Enter and leave each city exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_city_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_city_{i}"

# Solve the problem
status = problem.solve()

# Check the results
if pulp.LpStatus[status] == 'Optimal':
    tour = []
    current_city = 0
    visited_cities = [False] * n
    visited_cities[0] = True
    while len(tour) < n:
        tour.append(current_city)
        for j in range(n):
            if pulp.value(x[current_city, j]) == 1:
                current_city = j
                break

    tour.append(0)  # Complete the tour by returning to the depot

    tour_cost = sum(costs[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print("Tour:", tour)
    print("Total travel cost:", tour_cost)
else:
    print("The optimization problem did not solve successfully. Status:", pulp.LpStatus[status])
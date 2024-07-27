import pulp
import math

# Coordinates and Groups
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94),
    18: (51, 58), 19: (30, 48)
}
groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]
]


def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Prepare data
num_cities = len(cities)
all_cities = list(cities.keys())
num_groups = len(groups)
Vp = {i + 1: group for i, group in enumerate(groups)}
Vp[0] = [0]  # depot group
costs = {(i, j): euclidean_distance(cities[i], cities[j]) for i in all_cities for j in all_cities if i != j}

# Problem setting
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')

# Objective
problem += pulp.lpSum(costs[i, j] * x[i, j] for i in all_cities for j in all_cities if i != j), "Total Travel Cost"

# Constraints
# Group exit and re-entry
for p in range(1, num_groups + 1):
    problem += pulp.lpSum(x[i, j] for i in Vp[p] for j in all_cities if i != j) == 1, f"Leave_Group_{p}"
    problem += pulp.lpSum(x[i, j] for j in Vp[p] for i in all_cities if i != j) == 1, f"Enter_Group_{p}"

# For the depot group
problem += pulp.lpSum(x[0, j] for j in all_cities if j != 0) == 1, "Leave_Depot"
problem += pulp.lpSum(x[i, 0] for i in all_cities if i != 0) == 1, "Enter_Depot"

# Flow conservation
for k in all_cities:
    problem += (pulp.lpSum(x[j, k] for j in all_cities if j != k) == pulp.lpSum(x[k, j] for j in all_cities if j != k)), f"Flow_{k}"

# Solve the problem
problem.solve()

# Retrieve the results
tour = []
current_city = 0
visited = set([0])

while True:
    next_cities = [j for j in all_cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

tour.insert(0, 0)  # Start at the depot

# Calculate cost
tour_cost = sum(costs[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost}")
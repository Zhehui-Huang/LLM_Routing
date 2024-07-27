import pulp
import math

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

depots = [0, 1, 2, 3]
n_robots = 4

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a distance matrix
cost = {(i, j): euclidean_distance(cities[i], cities[j]) if i != j else float('inf') for i in cities for j in cities}

# Initiate Linear Programming Problem
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("travel", (cities.keys(), cities.keys(), depots), cat='Binary')
u = pulp.LpVariable.dicts("order", (cities.keys(), depots), lowBound=0, upBound=len(cities), cat='Continuous')

# Objective Function: Minimize the total cost
prob += pulp.lpSum(cost[i, j] * x[i, j, k] for i in cities for j in cities for k in depots), "Total cost"

# Constraints
for k in depots:
    prob += pulp.lpSum(x[k, j, k] for j in cities if j != k) == 1, f"Leave depot {k}"
    prob += pulp.lpSum(x[j, k, k] for j in cities if j != k) == 1, f"Return to depot {k}"

for j in cities:
    if j not in depots:
        prob += pulp.lpSum(x[i, j, k] for i in cities for k in depots if i != j) == 1, f"Visit city {j}"

for k in depots:
    for i in cities:
        prob += pulp.lpSum(x[i, j, k] for j in cities if j != i) == pulp.lpSum(x[j, i, k] for j in cities if j != i), f"Flow conservation at city {i}, depot {k}"

# Subtour Elimination
for k in depots:
    for i in cities:
        for j in cities:
            if i != j and i not in depots and j not in depots:
                prob += u[i, k] - u[j, k] + len(cities) * x[i, j, k] <= len(cities) - 1

# Solve the problem
status = prob.solve()
print("Status:", pulp.LpStatus[status])

# Collect results
total_cost = 0
for k in depots:
    tour = []
    for i in cities:
        for j in cities:
            if pulp.value(x[i, j, k]) == 1:
                tour.append((i, j))

    # Print the tour
    ordered_tour = [k]
    next_city = k

    while len(ordered_tour) < len(tour) + 1:
        for (i, j) in tour:
            if i == next_city:
                ordered_tour.append(j)
                next_city = j
                break

    tour_cost = sum(cost[ordered_tour[i], ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {ordered_tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")
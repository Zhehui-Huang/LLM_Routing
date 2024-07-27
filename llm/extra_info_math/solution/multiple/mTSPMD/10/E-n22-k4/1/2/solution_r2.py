import pulp
import math

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 352), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of cities and depots
n = len(cities)
depots = [0, 1, 2, 3]

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating a cost matrix
costs = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize the optimization problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x",
                          ((i, j, k) for i in range(n) for j in range(n) for k in depot),
                          cat='Binary')

# Objective Function
problem += pulp.lpSum(costs[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in depots)

# Constraints
for j in range(n):
    if j not in depots:
        problem += pulp.lpSum(x[i][j][k] for i in range(n) for k in depots) == 1

for k in depots:
    problem += pulp.lpSum(x[k][j][k] for j in range(n) if j != k) == 1
    problem += pulp.lpSum(x[j][k][k] for j in range(n) if j != k) == 1

for i in range(n):
    if i not in depots:
        for k in depots:
            problem += (pulp.lpSum(x[i][j][k] for j in range(n)) ==
                        pulp.lpSum(x[j][i][k] for j in range(n)))

# Execute the solver
problem.solve()

# Collect results
overall_travel_cost = 0

for k in depots:
    tour = [k]
    current_city = k
    visited = set(tour)

    while True:
        found_next_city = False
        for next_city in range(n):
            if next_city not in visited and pulp.value(x[current_city][next_city][k]) == 1:
                tour.append(next_city)
                visited.add(next_city)
                overall_travel_cost += costs[current_city][next_city]
                current_city = next_city
                found_next_city = True
                break
        if not found_next_city:
            overall_travel_cost += costs[current_city][k]
            tour.append(k)  # return to depot
            break

    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {sum(costs[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))}")

print(f"Overall Total Travel Cost: {overall_travel_cost}")
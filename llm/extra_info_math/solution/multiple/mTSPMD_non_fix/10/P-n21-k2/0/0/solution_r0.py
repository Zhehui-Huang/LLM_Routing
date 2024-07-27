import pulp
import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Parameters
num_robots = 2
depots = {0}
num_cities = len(cities)

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create the problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, cat='Continuous')

# Objective function
prob += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# Ensure each city is visited exactly once
for j in cities:
    prob += pulp.lpSum(x[i, j] for i in cities if i != j) == 1
    
# Ensure departure from each city exactly once
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1

# Subtour elimination
n = len(cities)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Output the results
tours = {robot: [] for robot in range(num_robots)}
costs = {robot: 0 for robot in range(num_robots)}

for k in range(num_robots):
    current_city = 0
    while True:
        next_cities = [j for j in cities if pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tours[k].append(next_city)
        costs[k] += euclidean_distance(current_city, next_city)
        current_city = next_city
        if current_city == 0:
            break

overall_cost = sum(costs.values())

for robot in range(num_robots):
    tours[robot].insert(0, 0)
    tours[robot].append(0)
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {costs[robot]}")

print(f"Overall Total Travel Cost: {overall_cost}")
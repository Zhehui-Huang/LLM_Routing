import pulp
import math

# Define the function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_b[0] - city_a[0])**2 + (city_b[1] - city_a[1])**2)

# City coordinates
cities = [
    (26, 60),   # City 0: Depot
    (73, 84),   # City 1
    (89, 36),   # City 2
    (15, 0),    # City 3
    (11, 10),   # City 4 ...
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)    # City 19
]

# Create the linear programming problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

n = len(cities)
# Create variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pulp.LpBinary)
d = pulp.LpVariable("d", lowBound=0)

# Objective function
prob += d, "Maximum distance"

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[i][j] for j in range(n) if i != j]) == 1
    prob += pulp.lpSum([x[j][i] for j in range(n) if i != j]) == 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * euclidean_distance(cities[i], cities[j]) <= d

# Subtour Elimination
subsets = range(2, n)
for s in range(2, n):
    for S in itertools.combinations(subsets, s):
        prob += pulp.lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solve problem
prob.solve()

# Output results
tour = []
current_city = 0
visited = [0] + [0]*(n-1)
while True:
    tour.append(current_city)
    visited[current_city] = 1
    next_cities = [(x[current_city][j].value(), j) for j in range(n) if j != current
                   continue
        if xij_val == 1:
            tour.append(j)
            max_distance = max(max_distance, euclidean_distance(cities[current_city], cities[j]))
            total_cost += euclidean_distance(cities[current_city], cities[j])
            current_city = j
            break

    if all(visited):
        break

# Append the depot city to complete the tour
tour.append(0)
total_cost += euclidean_distance(cities[current_city], cities[0])
max_distance = max(max_distance, euclidean_distance(cities[current_city], cities[0]))

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
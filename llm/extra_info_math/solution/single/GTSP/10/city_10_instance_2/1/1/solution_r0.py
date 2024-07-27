import pulp
import math

# Define the city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Define groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2],
}

# Calculate distances using Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Total number of cities including the depot
num_cities = len(cities)
all_cities = list(range(num_cities))

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), 
                          cat='Binary')

# Objective: Minimize the sum of distances
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in all_cities for j in all_cities if i != j)

# Constraints to ensure exactly one outgoing edge and one incoming edge for each group
for group in groups:
    cities_in_group = groups[group]
    other_cities = [c for c in all_cities if c not in cities_in_group]
    prob += pulp.lpSum(x[i, j] for i in cities_in_project for j in other_cities) == 1
    prob += pulp.lpSum(x[j, i] for i in cities_in_group for j in other_cities) == 1

# Flow conservation at each node
for c in all_cities:
    prob += (pulp.lpSum(x[i, c] for i in all_cities if i != c) -
             pulp.lpSum(x[c, j] for j in all_cities if j != c)) == 0

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", all_cities[1:], lowBound=0, upBound=(len(groups) - 1), cat='Continuous')
k = len(groups)
for i in all_cities[1:]:
    for j in all_cities[1:]:
        if i != j:
            prob += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve the problem
prob.solve()

# Output result
tour = []
current_city = 0
visited = set([0])

for _ in range(num_of_cities):
    next_cities = [j for j in all_cities if pulp.value(x[current_city, j]) == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append(next_city)
        visited.add(next_city)
        current_city = next_city

# Adding depot at the end to complete the tour
tour.append(0)

# Total cost calculation
total_distance = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)
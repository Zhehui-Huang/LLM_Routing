import math
import pulp

# Coordinates of each city, including the depot city (index 0)
coords = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
          (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
          (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Euclidean distance calculator
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Number of cities (including depot city)
n = len(coords)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create decision variables x_ij and cost dictionary c_ij
x = pulp.LpVariable.dicts("x", ((i,j) for i in range(n) for j in range(n) if i != j), cat='Binary')
c = {(i, j): euclidean_distance(coords[i], coords[j]) for i in range(n) for j in range(n) if i != j}

# Objective function
problem += pulp.lpSum(c[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Total_Cost"

# Adding constraints
# Each city must be left and entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"Enter_{j}"
    problem += pulp.lpSum(x[j, k] for k in range(n) if j != k) == 1, f"Leave_{j}"

# MTZ subtour elimination
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solving the problem
problem.solve()

# Extract the tour from the solution
tour = []
cur_city = 0
total_cost = 0

while True:
    next_cities = [j for j in range(n) if j != cur_city and pulp.value(x[cur_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    total_cost += euclidean_distance(coords[cur_city], coords[next_city])
    cur_city = next_city
    if cur_city == 0:
        break

# add the depot city at start and end
tour = [0] + tour

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
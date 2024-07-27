import pulp
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

n = len(cities)
dist_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = pulp.LpProblem("Traveling_Salesman_Problem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
prob += pulp.lpSum(dist_matrix[i][j] * x[i,j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour elimination constraints (using additional variables u and a large M)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
M = n**2
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + M*x[i, j] <= M - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current = 0
for _ in range(n):
    next_city = [j for j in range(n) if pulp.value(x[current,j]) == 1][0]
    tour.append(next_city)
    current = next_city
tour.append(0)  # return to the depot

# Calculate total cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
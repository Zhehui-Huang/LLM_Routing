import math
import pulp

# City coordinates given in the problem statement
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
n = len(cities)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Creating variables xij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints that ensure each city is arrived at and departed from just once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for k in range(3, n+1):
    for S in itertools.combinations(range(1, n), k):  # Subsets of 1 through n-1, of size k
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
problem.solve()

# Extracting the solution
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Include the depot city at both start and end
tour = [0] + tour + [0]

# Calculate the total travel cost
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output format
print("Tour:", tour)
print("Total travel cost:", total_cost)
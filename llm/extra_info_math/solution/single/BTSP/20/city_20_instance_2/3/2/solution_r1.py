import pulp
import math

# Define the locations of cities including the depot
locations = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Number of cities including depot
n = len(locations)

# Distance matrix calculation
distances = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Setup the PuLP problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_dist = pulp.LpVariable("max_distance", lowBound=0)

# Objective
prob += max_dist

# Constraints
# Each city is entered and left exactly once
for k in range(n):
    prob += pulp.lpSum(x[(i, k)] for i in range(n) if i != k) == 1
    prob += pulp.lpSum(x[(k, j)] for j in range(n) if k != j) == 1

# Subtour elimination constraints using Miller-Tucker-Zemlin (MTZ) formulation
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[(i,j)] <= n-1

# Drive maximum distance constraint for each city pair
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[(i, j)] <= max_dist

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Extracting the solution
if status == pulp.LpStatusOptimal:
    tour = []
    current_city = 0
    visited_cities = [False] * n
    visited_cities[0] = True

    max_distance = 0
    total_distance = 0

    for _ in range(n):
        for j in range(n):
            if j != current_city and pulp.value(x[(current_city, j)]) == 1:
                tour.append(j)
                max_distance = max(max_distance, distances[current_city][j])
                total_distance += distances[current_city][j]
                current_city = j
                break
        visited_cities[current_city] = True
    
    # Adding the depot to complete the tour
    tour.insert(0, 0)
    tour.append(0)
    total_distance += distances[current_city][0]

    # Output results
    print("Tour:", tour)
    print("Total travel travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)

else:
    print("No optimal solution found.")
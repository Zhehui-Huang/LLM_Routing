import pulp
import math
import itertools

# Define coordinates
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Number of cities including depot
n = len(coordinates)

# Function to calculate Euclidean distance
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
dist = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize LP problem
prob = pulp.LpProblem("TSP_MinMaxDistance", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if path goes from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Auxiliary variable to minimize the maximum distance traveled between two consecutive cities
z = pulp.LpVariable("MaxDistance", lowBound=0, cat='Continuous')

# Objective function
prob += z, "Minimize the maximum distance between consecutive cities"

# Constraints
# Each city must be left and entered exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Maximum distance constraint for the route between any two cities
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * dist[i][j] <= z, f"MaxDistConstraint_{i}_{j}"

# Subtour elimination
for s in range(2, n):  # Subsets of at least size 2
    for S in itertools.combinations(range(1, n), s):  # Exclude the depot for subtour constraints
        prob += pulp.lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
prob.solve()

# Check status
if prob.status == 1:
    # Extract the tour
    tour = [0]
    next_city = 0
    while len(tour) < n:
        for j in range(n):
            if pulp.value(x[next_city, j]) == 1:
                next_city = j
                tour.append(next_city)
                break
    tour.append(0)  # complete the loop by returning to the depot

    # Calculate the total cost and longest edge
    total_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    longest_edge = max(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    # Output results
    print(f'Tour: {tour}')
    print(f'Total travel cost: {total_cost:.2f}')
    print(f'Maximum distance between consecutive cities: {longest_edge:.2f}')
else:
    print("No optimal solution found.")
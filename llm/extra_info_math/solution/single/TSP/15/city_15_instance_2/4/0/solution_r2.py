import pulp
import math

# City coordinates
cities = [
    (54, 87),  # City 0: Depot
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Distance calculation function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities
n = len(cities)

# Distance matrix
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean+distance(cities[i], cities[j])

# Define the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective Function
problem += pulp.lpSum([distembrances[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
for i in range(n):
    # Must leave city i exactly once
    problem += pulp.lpSum([x[i, j] for j in range(n) if i != j and (i, j) in x]) == 1
    # Must enter city i exactly once
    problem += pulp.lpSum([x[j, i] for j in range(n) if i != j and (j, i) in x]) == 1

# Subtour elimination constraints
for k in range(2, n):
    for subset in itertools.combinations(range(1, n), k):  # start from 1 to exclude depot
        problem += pulp.lpSum([x[i, j] for i in subset for j in subset if i != j and (i, j) in x]) <= len(subset) - 1

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[status]}")

    # Extract the tour
    tour = []
    current_location = 0
    while len(tour) < n:
        tour.append(current_location)
        next_locations = [j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1]
        if not next_locations:
            break
        current_location = next_locations[0]
    tour.append(0)  # Return to the depot

    # Calculate total travel cost
    total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
else:
    print("No optimal solution found.")
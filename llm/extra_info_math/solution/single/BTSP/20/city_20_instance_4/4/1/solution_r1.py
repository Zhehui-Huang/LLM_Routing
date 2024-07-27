import pulp
import math
import itertools

# Set up the city coordinates
coordinates = [
    (26, 60),  # City 0 (Depot)
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
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
    (14, 89)   # City 19
]

n = len(coordinates)  # Number of cities

# Calculate the Euclidean distance between every pair of different cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = {
    (i, j): distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Instantiate the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_distance = pulp.LpVariable("Max_Distance", lowBound=0)

# Objective Function
problem += max_distance

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for i in range(n) if i != j) == 1
    
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i, j] <= max_distance

# Subtour elimination constraints
for l in range(2, n):
    for subset in itertools.combinations(range(1, n), l):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = problem.solve()

# Check the optimum status and then extract the tour details
if pulp.LpStatus[status] == "Optimal":
    non_zero_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    
    # Find the road trip path
    tour = [0]
    while len(tour) < n:
        for i, j in non_zero_edges:
            if i == tour[-1]:
                tour.append(j)
                break

    tour.append(0)  # to return to the depot
    total_distance_traveled = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    maximum_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total_distance_traveled)
    print("Maximum distance between consecutive cities:", maximum_distance)
else:
    print("No optimal solution found.")
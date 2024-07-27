import pulp
import math
import itertools

# Input data
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate distance matrix
n = len(cities)
distances = [[euclideanDistance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the pulp model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
Z = pulp.LpVariable("Z", lowBound=0, cat='Continuous')

# Objective function
model += Z

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Eliminate subtours
for k in range(3, n + 1):
    for subset in itertools.combinations(range(1, n), k):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Linking variable Z to the maximum of any selected distance
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[i, j] <= Z

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
if pulp.LpStatus[status] == 'Optimal':
    tour = [0]
    current_city = 0
    max_distance = 0
    for _ in range(n-1):
        next_cities = {j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1}
        if not next_cities:
            break
        next_city = next_cities.pop()
        max_distance = max(max_distance, distances[current_city][next_city])
        tour.append(next_city)
        current_city = next_city
    tour.append(0)  # Return to starting point
    total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")

else:
    print("No optimal solution found.")
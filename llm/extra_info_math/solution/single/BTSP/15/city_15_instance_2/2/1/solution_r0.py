import pulp
import math

# Define the cities with their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

n = len(cities)

# Calculate distances between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the problem
prob = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Create variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 0, 1, pulp.LpBinary)
d_max = pulp.LpVariable("d_max", lowBound=0)

# Objective function
prob += d_release

# Add the constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # leaving i
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # entering i

for i in range(1, len(cities)):
    subtours = [[j for j in cities if j != i] for i in range(1, len(cities))]
    for s in subtours:
        if len(s) > 1:
            prob += pulp.lpSum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1

# Linking max distance to distances
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * distances[i, j] <= d_max

# Solve the problem
if prob.solve() == pulp.LpStatusOptimal:
    tour = []
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))

    # Sort the tour to start at city 0 and end at city 0
    current_city = 0
    sorted_tour = [current_city]
    while len(sorted_tour) < len(cities):
        for next_city in tour:
            if next_city[0] == current_city:
                current_city = next_city[1]
                sorted_tour.append(current_city)
                break

    # Compute total travel cost and maximum distance
    total_distance = sum(distances[tour[i], tour[i + 1]] for i in range(len(cities) - 1))
    max_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(cities) - 1))

    print(f"Tour: {sorted_tour + [0]}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution found.")
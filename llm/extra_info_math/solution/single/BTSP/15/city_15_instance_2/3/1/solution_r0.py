import numpy as np
import pulp

# Given city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
num_cities = len(cities)

# Calculate distances
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Integer programming model
model = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), 
                          cat=pulp.LpBinary)
d = pulp.LpVariable("d", lowBound=0, cat=pulp.LpContinuous)

# Objective: minimize the maximum distance traveled between any two cities
model += d

# Constraints
for i in range(num_cities):
    model += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(num_cities) if i != j) == 1

# Link x and d
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            model += x[i, j] * distances[(i, j)] <= d

# Subtour Elimination
from itertools import combinations
for s in range(2, num_cities):
    for S in combinations(range(1, num_cities), s):  # skip the depot city for subsets
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=0))
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    tour = []
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))
    # Organizing the tour starting from the depot
    organized_tour = [0]
    while len(organized_tour) < num_cities:
        for (i, j) in tour:
            if i == organized_tour[-1]:
                organized_tour.append(j)
                tour.remove((i, j))
                break
    organized_tour.append(0)  # return to depot
    total_travel_cost = sum(distances[(organized_tour[i], organized_tour[i+1])] for i in range(num_cities))
    max_distance = max(distances[(organized_tour[i], organized_tour[i+1])] for i in range(num_cities))

    print(f"Tour: {organized_tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution.")
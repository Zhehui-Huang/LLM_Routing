import numpy as, np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

model = LpProblem("TSP", LpMinimize)

x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)

model += lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if j != i) == 1
    model += lpSum(x[j, i] for j in range(n) if j != i) == 1

for S in range(2, n):
    for subsets in combinations(range(1, n), S):
        model += lpSum(x[i, j] for i in subsets for j in subsets if i != j) <= len(subsets) - 1

model.solve()

tour = []
visited = [False]*n
current = 0
count = 0

while not all(visited) and count < n:
    visited[current] = True
    tour.append(current)
    next_cities = [j for j in range(n) if x[current, j].value() == 1 and not visited[j]]
    if next_cities:
        current = next_cities[0]
    count += 1

tour.append(0)  # complete the loop back to the depot

total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
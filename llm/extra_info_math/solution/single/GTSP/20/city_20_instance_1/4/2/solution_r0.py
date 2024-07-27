import pulp
from math import sqrt

# City coordinates
coords = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Calculate the Euclidean distance between each pair of cities
def distance(i, j):
    return sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Decision variables: x_ij = 1 if travel from city i to city j, 0 otherwise
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j) for i in coords for j in coords if i != j], cat='Binary')

# Objective Function
model += pulp.lpSum(distance(i, j) * x[(i, j)] for i in coords for j in coords if i != j)

# Constraints
# Exactly one city from each group must be selected
for group in groups:
    model += sum(x[(0, j)] for j in group) == 1
    model += sum(x[(j, 0)] for j in group) == 1

# Subtour elimination constraints (2 and 3):
for i in coords:
    model += sum(x[(j,i)] for j in coords if i != j) == sum(x[(i,j)] for j in coords if i != j)

# Solve the problem
model.solve()

# Extract the tour
tour = [0]
current = 0
visited = set([0])

while True:
    next_city = None
    for j in coords:
        if pulp.value(x[(current, j)]) == 1:
            next_city = j
            break
    if next_city == 0:
        tour.append(0)
        break
    tour.append(next_city)
    current = next_city

# Calculate the total cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
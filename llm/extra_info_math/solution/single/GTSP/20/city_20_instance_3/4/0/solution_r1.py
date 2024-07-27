import pulp
import math

# Coordinates of all cities including depot city 0
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Euclidean distance calculation
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Variables
model = pulp.LpProblem("TSP_Grouped_Cities", pulp.LpMinimize)
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective function
model += pulp.lpSum(x[i, j] * dist(i, j) for i in cities for j in cities if i != j)

selected_cities = [0]  # Include the depot city

# Constraints to ensure exactly one city from each group is included
for group in groups:
    model += pulp.lpSum(x[0, j] for j in group) == 1  # From depot to group
    model += pulp.lpSum(x[j, 0] for j in group) == 1  # From group to depot
    selected_cities += group

# Subtour constraint that ensures leaving every city and returning
for k in selected_cities:
    model += pulp.lpSum(x[k, j] for j in selected_cities if j != k) == 1
    model += pulp.lpSum(x[j, k] for j in selected_cities if j != k) == 1

# Solve the model
if model.solve() == pulp.LpStatusOptimal:
    total_cost = pulp.value(model.objective)
    tour = []
    # Extract the tour from decision variables
    current = 0
    while True:
        tour.append(current)
        next_city = [j for j in selected_cities if pulp.value(x[current, j]) == 1]
        if not next_city:
            break
        current = next_city[0]
        if current == 0:
            break
    tour.append(0)  # Complete the loop back to depot
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Optimal solution not found.")
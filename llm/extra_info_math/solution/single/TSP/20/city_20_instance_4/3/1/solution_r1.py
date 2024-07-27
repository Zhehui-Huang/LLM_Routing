import pulp
import math
import itertools

# City positions
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

n = len(cities)

# Calculate Euclidean distance between cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Setting up the TSP Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    model += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1
    model += pulp.lpSum(x[(j, i)] for j in cities if i != j) == 1

# Subtour Elimination
subtours = []
for i in range(2, n):
    for subset in itertools.combinations(cities.keys(), i):
        if 0 in subset:  # Ensure depot is in the subset
            subtours.append(subset)
for subtour in subtours:
    model += pulp.lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extracting the solution
tour = [0]
current_city = 0
for _ in range(n - 1):
    next_cities = [(j, x[(current_city, j)].varValue) for j in cities if j != current_city]
    next_city = next(filter(lambda x: x[1] == 1, next_cities))[0]
    tour.append(next_city)
    current_city = next_city

if status == 1:  # Check if the model is solved successfully
    tour.append(0)  # back to the depot
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {round(total_cost, 2)}")
else:
    print("The problem did not solve successfully")
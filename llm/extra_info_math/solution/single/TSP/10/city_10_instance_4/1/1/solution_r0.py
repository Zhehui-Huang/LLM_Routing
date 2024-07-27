import pulp
import math

# Coordinates of the cities
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of cities
n = len(cities)

# Cost matrix
cost = {(i, j): euclidean_distance(i, j) for i in cities.keys() for j in cities.keys() if i != j}

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", cost.keys(), 0, 1, pulp.LpBinary)

# Objective function
model += pulp.lpSum([cost[i, j] * x[i, j] for i, j in cost.keys()]), "Total Travel Cost"

# Constraints
for k in cities.keys():
    model += pulp.lpSum([x[i, j] for i, j in cost.keys() if i == k]) == 1, f"Leave_city_{k}"
    model += pulp.lpSum([x[i, j] for i, j in cost.keys() if j == k]) == 1, f"Enter_city_{k}"

# Subtour Elimination Constraints
for i in range(2, n):  
    subSets = itertools.combinations(list(cities.keys())[1:], i)
    for S in subSets:
        model += pulp.lpSum([x[i, j] for i in S for j in S if (i, j) in x]) <= len(S) - 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract solution
if status == pulp.LpStatusOptimal:
    tour = []
    current_position = 0
    while len(tour) < len(cities):
        tour.append(current_position)
        for j in cities:
            if pulp.value(x[current_position, j]) == 1:
                current_position = j
                break
    tour.append(0)  # To return to the starting point

    # Total cost calculation
    total_cost = sum([cost[tour[i], tour[i+1]] for i in range(len(tour)-1)])

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No optimal solution found.")
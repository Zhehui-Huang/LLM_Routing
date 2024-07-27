import pulp
import math

# Coordinates of the cities
coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Cities
cities = list(coordinates.keys())

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = {}
for i in cities:
    for j in cities:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective
model += pulp.lpSum(distance(i, j) * x[(i, j)] for i in cities for j in cities if i != j)

# Constraints
# Each city is left exactly once
for i in cities:
    model += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1

# Each city is entered exactly once
for j in cities:
    model += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1

# Subtour elimination constraints (using MTZ)
u = {}
for i in cities:
    if i != 0:  # Depot city does not need a position variable
        u[i] = pulp.LpVariable(f"u_{i}", lowBound=1, cat='Continuous')

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + len(cities) * x[(i, j)] <= len(cities) - 1

# Solve model
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

if pulp.LpStatus[status] == 'Optimal':
    print("Found optimal solution.")
    print(f"Total travel cost: {pulp.value(model.objective)}")
    
    # Construct tour from variables
    tours = []
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[(i, j)]) == 1:
                tours.append((i, j))
    
    # Order the tour starting from the depot
    current_location = 0
    tour = [current_location]
    while len(tours) > 0:
        for i, j in tours:
            if i == current_location:
                tour.append(j)
                current_location = j
                tours.remove((i, j))
                break
    
    # Return to depot
    tour.append(0)
    print(f"Tour: {tour}")
else:
    print("Failed to find optimal solution.")
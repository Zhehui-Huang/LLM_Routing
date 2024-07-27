import pulp
import math

# Define city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate Euclidean distances between cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of Robots
m = 4

# Model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(len(coordinates))
                                for j in range(len(coordinates)) if i != j
                                for k in range(m)), cat='Binary')

u = pulp.LpVariable.dicts("u", ((i) for i in range(1, len(coordinates))),
                          lowBound=0, cat='Continuous')

# Objective
model += pulp.lpSum(x[(i, j, k)] * distance(coordinates[i], coordinates[j])
                    for i in range(len(coordinates))
                    for j in range(len(coordinates)) if i != j
                    for k in range(m)), "Total Distance"

# Constraints
# Each city must be visited exactly once by exactly one salesman
for j in range(1, len(coordinates)):
    model += pulp.lpSum(x[(i, j, k)] for i in range(len(coordinates)) if i != j
                        for k in range(m)) == 1

# Enter and leave each city
for k in range(m):
    for j in range(1, len(coordinates)):
        model += pulp.lpSum(x[(i, j, k)] for i in range(len(coordinates)) if i != j) == \
                 pulp.lpSum(x[(j, i, k)] for i in range(len(coordinates)) if i != j)

# Each salesman starts from the depot
for k in range(m):
    model += pulp.lpSum(x[(0, j, k)] for j in range(1, len(coordinates))) == 1

# Subtour elimination
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            for k in range(m):
                model += (u[i] - u[j] + (len(coordinates) - 1) * x[(i, j, k)]) <= (len(coordinates) - 2)

# Solve the model
model.solve()

# Output tours and costs
tours = {k: [] for k in range(m)}
for k in range(m):
    tour = [0]
    while True:
        j = next(j for i, j in enumerate(coordinates) if i != tour[-1] and pulp.value(x[(tour[-1], i, k)]) == 1)
        if j == 0:
            break
        tour.append(j)
    tours[k] = tour + [0]

for k, tour in tours.items():
    cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

max_cost = max(sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
               for tour in tours.values())
print(f"Maximum Travel Cost: {max_cost}")
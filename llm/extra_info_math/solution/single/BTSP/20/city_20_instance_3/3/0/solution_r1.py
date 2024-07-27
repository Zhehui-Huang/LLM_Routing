import math
import pulp

# Define the coordinates of the cities
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

n = len(city_coords)  # Number of cities

# Function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(city_coords[i], city_coords[j])

# Initialization of the problem
model = pulp.LpProblem("Minimize_Max_Distance_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)
d_max = pulp.LpVariable("d_max", lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance
model += d_max

# Constraints for incoming and outgoing flows
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Avoiding sub-tours using positional variables
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Ensuring d_max is the maximum distance
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[(i, j)] * x[(i, j)] <= d_max

# Solving the model
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Organize the results
tour = []
current_city = 0
for _ in range(n):
    tour.append(current_city)
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    current_city = next_cities[0] if next_cities else tour[0]

tour.append(0)  # Complete the tour by returning to the depot

# Calculate total and maximum travel costs
total_travel_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(n))
max_travel_distance = max(distances[(tour[i], tour[i + 1])] for i in range(n))

# Print the output as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_travel_dice}")
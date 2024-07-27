import pulp
import math

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Input data for the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

num_cities = len(cities)

# Create a problem instance
prob = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Creating decision variable
x = {}
for i in cities:
    for j in cities:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Distance maximum variable
max_dist = pulp.LpVariable("Max_Distance", lowBound=0)

# Objective function
prob += max_dist

# Constraints to ensure each city is entered and left only once
for i in cities:
    prob += sum(x[(i, j)] for j in cities if i != j) == 1, f"Sum_of_outflows_{i}"
    prob += sum(x[(j, i)] for j in cities if i != j) == 1, f"Sum_of_inflows_{i}"

# Sub-tour elimination constraints
order = []
for i in range(num_cities):
    order.append(pulp.LpVariable(f"order_in_tour{str(i)}", cat='Continuous'))

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += order[i] - order[j] + num_cities * x[(i, j)] <= num_cities - 1

# Constraint to compute the maximum distance
for i in cities:
    for j in cities:
        if i != j:
            prob += x[(i, j)] * calculate_distance(cities[i], cities[j]) <= max_dist

# Solve the LP
prob.solve()

# Extract tour using the decision variables
tour = [0]
while len(tour) < num_cities:
    for j in cities:
        if j != tour[-1] and pulp.value(x[(tour[-1], j)]) == 1:
            tour.append(j)
            break

# Append start city to end route
tour.append(0)

# Calculate the total cost and maximum distance
total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
max_distance = max(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
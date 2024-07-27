import pulp
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define city coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}
n = len(cities)
m = 8 # Number of robots

# Create the problem instance
model = pulp.LpProblem("Vehicle_Routing_Problem", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat='Binary')

# Objective Function
model += pulp.lpSum(x[(i, j, k)] * calculate_distance(cities[i], cities[j]) for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints
for k in range(m):
    model += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1  # Robots start at the depot

# Every city must be visited exactly once
for j in range(1, n):
    model += pulp.lpSum(x[(i, j, k)] for k in range(m) for i in range(n) if i != j) == 1  # Enter
    model += pulp.lpSum(x[(j, i, k)] for k in range(m) for i in range(n) if i != j) == 1  # Leave

# Flow conservation
for k in range(m):
    for j in range(1, n):
        model += (
            pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) -
            pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j)) == 0

# Solve the problem
model.solve()

# Extract solution
tours = {k: [] for k in range(m)}
for k in range(m):
    tour = [0]  # start at the depot
    next_city = None
    while True:
        next_cities = [j for j in range(n) if j not in tour and pulp.value(x[(tour[-1], j, k)]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
    tour.append(0) # end at the depot
    tours[k] = tour

# Calculate and display results
overall_cost = 0
for k in tours:
    tour = tours[k]
    tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    overall_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")
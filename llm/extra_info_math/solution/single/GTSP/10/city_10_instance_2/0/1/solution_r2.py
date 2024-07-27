import math
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value, LpBinary

# Defined city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Definition of city groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to compute Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Set up the optimization problem
prob = LpProblem("Minimize_Tour_Length", LpMinimize)

# Decision variables
x = {(i, j): LpVariable(f"x_{i}_{j}", cat=LpBinary) for i in cities for j in cities if i != j}

# Objective Function
prob += lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# Only one city per group must be visited each way
for g in groups.values():
    prob += lpSum(x[i, j] for i in g for j in cities if j not in g) == 1, f"One_Exit_Per_Group_{g}"
    prob += lpSum(x[j, i] for i in g for j in cities if j not in g) == 1, f"One_Entry_Per_Group_{g}"

# Flow conservation at each node
for k in cities:
    prob += lpSum(x[i, k] for i in cities if i != k) == lpSum(x[k, j] for j in cities if j != k), f"Flow_Conservation_in_{k}"

# Resolve the problem
prob.solve()

# Extract the tour
tour = [0]
current_city = 0
while len(tour) < len(groups) + 1:
    next_cities = [(j, cities[j]) for j in cities if value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0][0]
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # return to the depot

# Calculate total travel cost
total_travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

tour_output = "Tour: " + str(tour)
cost_output = "Total travel cost: " + str(total_travel_cost)

tour_output, cost_output
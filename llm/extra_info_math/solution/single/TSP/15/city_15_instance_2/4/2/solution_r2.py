import math
import pulp
from itertools import product

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates for the cities including the depot city at index 0
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
    14: (6, 99),
}

n = len(coordinates)  # including the depot

# Problem variable
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variable, x[i,j] is 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: minimize the total distance travelled
problem += pulp.lpSum(x[i, j] * euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j)

# Each city has exactly one departure
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"One_out_{i}"

# Each city has exactly one arrival
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"One_in_{j}"

# Subtour elimination using the Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
problem.solve()

# Retrieve solution
tour = []
current_city = 0
next_city = None
for _ in range(n):
    tour.append(current_city)
    next_city = next(j for j in range(n) if i != j and pulp.value(x[current_city, j]) == 1)
    current_city = next_city
    if current_city == 0:
        break

tour.append(0)  # return to depot

# Calculate the total travel cost
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Print the output in the format requested
print("Tour:", tour)
print("Total travel cost:", total_cost)
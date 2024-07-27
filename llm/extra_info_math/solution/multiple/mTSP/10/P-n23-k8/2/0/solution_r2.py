import pulp
import math

# Define the problem parameters
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

n = len(cities)
m = 8

# Create the problem instance
prob = pulp.LpProblem("VRP_Multi_Depot", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective: Minimize the total travel cost
prob += pulp.lpSum(distance(cities[i], cities[j]) * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Ensure every city is visited exactly once by exactly one vehicle
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Departing and returning to the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation for other cities
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination (avoiding loops within the tour)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n * x[i, j, k]) <= n - 1

# Solve the problem
prob.solve()

# Output results
total_cost = 0
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                tour.append((i, j))
    organized_tour = [0]
    while tour:
        for i, t in enumerate(tour):
            if t[0] == organized_tour[-1]:
                organized_tour.append(t[1])
                tour.pop(i)
                break
    tour_cost = sum(distance(cities[organized_tour[i]], cities[organized_tour[i+1]]) for i in range(len(organized_tour)-1))
    print(f"Robot {k} Tour: {organized_tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")
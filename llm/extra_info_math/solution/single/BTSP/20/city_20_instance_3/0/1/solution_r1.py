import pulp
import itertools
import math

# Coordinates of city locations including the depot
cities = [
    (30, 56),   # City 0 (Depot)
    (53, 42),   # City 1
    (1, 95),    # City 2
    (25, 61),   # City 3
    (69, 57),   # City 4
    (6, 58),    # City 5
    (12, 84),   # City 6
    (72, 77),   # City 7
    (98, 95),   # City 8
    (11, 0),    # City 9
    (61, 25),   # City 10
    (52, 0),    # City 11
    (60, 95),   # City 12
    (10, 94),   # City 13
    (96, 73),   # City 14
    (14, 47),   # City 15
    (18, 16),   # City 16
    (4, 43),    # City 17
    (53, 76),   # City 18
    (19, 72)    # City 19
]

n = len(cities)

# Create the linear programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Distance calculation between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')
d = pulp.LpVariable("MaxDistance", lowBound=0, cat='Continuous')

# Objective function to minimize the maximum distance
model += d, "Minimize_Maximum_Distance"

# Constraints for entering and leaving each city
for i in range(n):
    model += sum(x[i, j] for j in range(n) if i != j) == 1
    model += sum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints to prevent loops
for m in range(2, n):
    for S in itertools.combinations(range(1, n), m):
        model += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Distance constraints linking variables with objective
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distance(cities[i], cities[j]) <= d

# Solve the problem
model.solve()

# Extract the tour from the solved model
tour = [0]
current = 0
for _ in range(n-1):
    next_city = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1][0]
    tour.append(next_city)
    current = next_city

# Close the tour returning to the depot
tour.append(0)

# Calculate the total distance and max distance between consecutive cities
total_distance = 0
max_consecutive_distance = 0
for i in range(len(tour)-1):
    dist = distance(cities[tour[i]], cities[tour[i+1]])
    total_distance += dist
    max_consecutive_distance = max(max_consecutive_distance, dist)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")
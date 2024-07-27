import pulp
import math
from itertools import product

# Coordinates of cities including the depot city
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including a depot
n = len(coordinates)

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create the LP problem instance
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Binary variables which indicate the selected path
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i, j in product(range(n), range(n)) if i != j),
                          cat='Binary')

# Objective function to minimize the total distance
model += pulp.lpSum(distance(i, j) * x[i, j] for i, j in product(range(n), range(n)) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour Elimination Constraints
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

if pulp.LpStatus[model.status] == 'Optimal':
    next_city = 0
    tour = [next_city]
    cost = 0
    while True:
        next_cities = [j for j in range(n) if j != next_city and pulp.value(x[next_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        if next_city == 0:
            break

    # Closing the tour by coming back to the starting point
    if tour[-1] != 0:
        tour.append(0)

    # Calculate the travel cost of this tour
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("No optimal solution found.")
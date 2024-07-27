import pulp
import math
from itertools import combinations

# Coordinates of cities including the depot city
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities including the depot
n = len(coordinates)

# Distance function (Euclidean)
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create a LP Problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective
model += pulp.lpSum(distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination constraints
for k in range(2, n):
    for S in combinations(range(1, n), k):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve()

# Retrieve solution if optimal solution found
if pulp.LpStatus[model.status] == 'Optimal':
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append(i)
                break
            
    tour.append(0)  # complete the tour by returning to the depot

    # Calculate the cost of the tour
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour__);
else:
    print("No optimal solution found")
import math
from pulp import *
import itertools

# Coordinates of the 15 cities including the depot city 0
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities (including the depot)
n = len(coordinates)

# Create the problem variable to contain the problem data
problem = LpProblem("MinimizeMaxDistanceTSP", LpMinimize)

# Decision variables: x[i, j] is 1 if the path goes from city i to city j
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Variable to minimize: maximum distance between any two consecutive cities
max_distance = LpVariable("max_distance")

# Objective function
problem += max_distance, "Longest distance of any segment in the tour"

# Constraints for entering and leaving each city
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_city_{i}"
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_city_{i}"

# Subtour elimination constraints
for s in range(3, n+1):
    for subtour in itertools.combinations(range(1, n), s):
        problem += lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Max distance constraint linking
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance(i, j) <= max_distance

# Solve the problem
problem.solve()

# Extract the tour order from the decision variables
tour = []
current_city = 0
for _ in range(n):
    tour.append(current_mode)
    next_city = next(j for j in range(n) if j != current_city and value(x[current_city, j]) == 1)
    current_city = next_city
tour.append(0)  # Close the loop back to depot city

# Compute total travel cost and maximum distance between consecutive cities
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_segment_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_segment_distance)
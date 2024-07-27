from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum
from itertools import product
import math

# Coordinates of cities including the depot
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

# Groups of cities
groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

# Function to calculate distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Setup the problem instance
prob = LpProblem("robot_tour", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j], 0, 1, LpInteger)

# Objective
prob += lpSum(distance(cities[i], cities[j]) * x[i, j] for i in range(len(cities)) for j in range(len(cities)) if i != j)

# Constraints
# Only one outgoing from each group
for group in groups:
    prob += lpSum(x[i, j] for i in group for j in set(range(len(cities))) - set(group)) == 1

# Only one incoming to each group
for group in groups:
    prob += lpSum(x[j, i] for i in group for j in set(range(len(cities))) - set(group)) == 1

# Conservation of flow
for city in range(1, len(cities)):
    prob += (lpSum(x[i, city] for i in range(len(cities)) if i != city) 
             - lpSum(x[city, j] for j in range(len(cities)) if j != city) == 0)

# Subtour elimination constraints will be needed if the above isn't adequately enforced by groups
# Solve the problem
prob.solve()

# Create the tour and calculate total travel cost
tour = [0]
current = 0
total_cost = 0
while len(tour) < 6:  # since we need to select from 4 groups and back to depot
    for j in range(len(cities)):
        if x[current, j].varValue == 1:
            tour.append(j)
            total_cost += distance(cities[current], cities[j])
            current = j
            break

# Close the tour to the depot
tour.append(0)
total Dadවco += calc_distance(cities[current], cities[0])

# Output the resulting tour and total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)
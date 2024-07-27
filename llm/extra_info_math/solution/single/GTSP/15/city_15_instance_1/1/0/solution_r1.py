from pulp import LpProblem, LpMinimize, LpVariable, LpInteger, lpSum, LpStatus
import math

# Coordinates of cities including the depot
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

# Groups of cities
groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize the problem
prob = LpProblem("robot_tour", LpMinimize)

# Variables - x[i,j] will be 1 if the tour goes from city i to city j, 0 otherwise
x = LpVariable.dicts("x", [(i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j], 0, 1, LpInteger)

# Objective function: minimize the sum of distances for the tour
prob += lpSum(distance(cities[i], cities[j]) * x[i, j] for i in range(len(cities)) for j in range(len(cities)) if i != j)

# Each group must be visited once
for group in groups:
    prob += lpSum(x[i, j] for i in group for j in set(range(len(cities))) - set(group)) == 1
    prob += lpSum(x[j, i] for i in group for j in set(range(len(cities))) - set(group)) == 1

# Ensure that there is a continuous tour, handling the flow of travel
for k in range(1, len(cities)):
    prob += lpSum(x[i, k] for i in range(len(cities)) if i != k) == lpSum(x[k, j] for j in range(len(cities)) if j != k)

# Solving the problem
prob.solve()

# Check if a valid result has been found
if LpStatus[prob.status] == 'Optimal':
    # Extract the route from the solution
    tour = [0]
    current_city = 0
    total_cost = 0
    for _ in range(len(groups) + 1): # Visit one city from each group + return to depot
        next_city = next(j for j in range(len(cities)) if j != current_city and x[current_city, j].varValue == 1)
        tour.append(next_city)
        total_cost += distance(cities[current_city], cities[next_city])
        current_city = next_city

    # Append return to the depot
    tour.append(0)
    total_cost += distance(cities[current_city], cities[0])

    # Display results
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("Failed to find an optimal solution.")
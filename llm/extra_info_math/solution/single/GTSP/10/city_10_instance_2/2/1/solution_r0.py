import pulp
import numpy as np
from math import sqrt

# Define the cities' coordinates
coordinates = {
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

# Define city groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Compute the Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create a list of all cities and a group map
all_cities = list(coordinates.keys())
city_to_group = {city: group for group, cities in groups.items() for city in cities}
num_groups = len(groups)

# Create the mixed integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j], cat='Binary')  # travel selections
u = pulp.LpVariable.dicts("u", range(num_groups), lowBound=0, cat='Continuous')  # for subtour elimination

# Objective Function
model += pulp.lpSum([distance(i, j) * x[i, j] for i in all_cities for j in all_cities if i != j]), "Total_Travel_Cost"

# Constraints
# Each group must have exactly one exit and one entry
for group, cities in groups.items():
    model += pulp.lpSum([x[i, j] for i in cities for j in all_cities if j not in cities]) == 1, f"One_exit_from_group_{group}"
    model += pulp.lpSum([x[j, i] for i in cities for j in all_cities if j not in cities]) == 1, f"One_entry_to_group_{group}"

# Flow conservation at each city
for k in all_cities:
    model += (pulp.lpSum([x[i, k] for i in all_cities if i != k]) == pulp.lpSum([x[k, j] for j in all_cities if j != k])), f"Flow_conservation_{k}"

# Subtour elimination
for g1 in range(1, num_groups):
    for g2 in range(1, num_groups):
        if g1 != g2:
            model += (u[g1] - u[g2] + num_groups * sum(x[i, j] for i in groups[g1] for j in groups[g2]) + 
                      (num_groups-2) * sum(x[j, i] for i in groups[g1] for j in groups[g2]) <= num_groups - 1)

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Output
if status == pulp.LpStatusOptimal:
    print("Tour:", end=" [")
    current_city = 0
    visited = set([current_city])
    tour = [current_city]
    
    # Build the tour from the variables
    while True:
        next_cities = [j for j in all_cities if j not in visited and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(nextCity)
        visited.add(next_city)
        current_city = nextCity
    tour.append(0)  # return to the depot
    print(", ".join(map(str, tour)) + "]")
    
    print("Total travel cost:", pulp.value(model.objective))
else:
    print("No optimal solution found.")
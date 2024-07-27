import math
import pulp

# City coordinates
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Calculating Euclidean distances between every pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city22[0])**2 + (city1[1] - city2[1])**2)

distances = {}
for i in city_coords:
    for j in city_coords:
        if i != j:
            distances[(i, j)] = euclidean_distance(city_coords[i], city_coords[j])

# Setting up the problem: Minimize total distance
problem = pulp.LpProblem("Select_Exactly_One_From_Each_Group_and_Minimize_Distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in city_coords for j in city_coords if i != j), 
                         cat=pulp.LpBinary)

# Objective
problem += pulp.lpSum(distances[(i, j)] * x[(i, j)] for i in city_coords for j in city_coords if i != j), "Minimize_Total_Distance"

# Constraints
# Exactly one city from each group must be chosen, plus entry and return to the depot
for group in city_groups.values():
    problem += pulp.lpSum(x[(0, j)] for j in group) == 1
    problem += pulp.lpSum(x[(j, 0)] for j in group) == 1
    
for group in city_groups.values():
    for node in group:
        problem += pulp.lpSum(x[(i, node)] for i in city_coords if i not in group) == 1
        problem += pulp.lpSum(x[(node, j)] for j in city_coords if j not in group) == 1

# Subtour elimination
N = len(city_coords) - 1  # excluding the depot
u = pulp.LpVariable.dicts("u", range(1, len(city_coords)), lowBound=0, upBound=N, cat=pulp.LpInteger)
for i in range(1, len(city_coords)):
    for j in range(1, len(city_coords)):
        if i != j:
            problem += u[i] - u[j] + len(city_coords) * x[(i, j)] <= len(city_coords) - 1

# Solve the problem
problem.solve()

# Extracting the solution
tour = [0]
for j in range(1, len(city_coords)):
    current = next(i for i in city_coords if i == tour[-1])
    next_city = next(j for j in city_coords if x[(current, j)].varValue == 1)
    if next_city != 0:
        tour.append(next

# Formatting the output
tour.append(0)  # Returning to the depot
total_travel_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
import pyomo.environ as pyo
from math import sqrt

# Coordinates of the cities indexed by city number
coordinates = {
    0: (30, 40),  # Depot
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate the Euclidean distance between two cities
def distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Set of all cities
cities = set(coordinates.keys())

# Optimization model
model = pyo.ConcreteModel()

# Variables
model.x = pyo.Var(cities, cities, within=pyo.Binary)  # Travel decision
model.u = pyo.Var(cities, within=pyo.NonNegativeReals)  # Tour position

# Objective: Minimize the total travel distance
model.obj = pyo.Objective(
    expr=sum(model.x[i, j] * distance(i, j) for i in cities for j in cities if i != j),
    sense=pyo.minimize
)

# Constraints
# Each city is visited and departed exactly once
def city_visit_once(model, j):
    return sum(model.x[i, j] for i in cities if i != j) == 1
model.city_visited = pyo.Constraint(cities, rule=city_visit_once)

def city_depart_once(model, i):
    return sum(model.x[i, j] for j in cities if i != j) == 1
model.city_departed = pyo.Constraint(cities, rule=city_depart_once)

# Sub-tour elimination
def subtour_elimination(model, i, j):
    if i != j:
        return model.u[i] - model.u[j] + len(cities) * model.x[i, j] <= len(cities) - 1
    return pyo.Constraint.Skip
model.no_subtours = pyo.Constraint(cities, cities, rule=subtour_elimination)

# Solver
solver = pyo.SolverFactory('glpk')
result = solver.solve(model)

# Extract tours
routes = {}
for i in cities:
    for j in cities:
        if pyo.value(model.x[i, j]) > 0.5:
            if i in routes:
                routes[i].append(j)
            else:
                routes[i] = [j]

# Find the starting city (depot)
current = 0  # Assuming the depot city '0' as the start
tours = []
visited = set()
while True:
    start = current
    tour = [start]
    while True:
        next_cities = routes.get(current, [])
        if not next_cities:
            break
        next_city = next_cities[0]
        if next_city in visited:
            break
        visited.add(next_city)
        tour.append(next_city)
        current = next_city
    if tour == [start]:
        break
    tours.append(tour)
    current = set(routes.keys()) - visited
    if not current:
        break
    current = min(current)

# Calculate and display the costs
total_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")
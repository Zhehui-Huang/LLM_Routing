import numpy as np
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, RangeSet, minimize, NonNegativeReals

# Data: Coordinates of the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

n = len(cities)  # Number of cities

# Function to calculate Euclidean distance
def distance(i, j):
    return np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create an instance of a model
model = ConcreteModel()
model.edges = Var(RangeSet(0, n-1), RangeSet(0, n-1), domain=NonNegativeReals)
model.max_link = Var(domain=NonNegativeReals)

# Objective: minimize the maximum distance traveled between any two consecutive cities
model.obj = Objective(expr=model.max_link, sense=minimize)

# Constraints
def city_outgoing(m, i):
    if i == 0:
        return sum(m.edges[i,j] for j in range(n) if i != j) == 2
    else:
        return sum(m.edges[i,j] for j in range(n) if i != j) == 1
model.out_con = Constraint(RangeSet(0,n-1), rule=city_outgoing)

def city_incoming(m, j):
    if j == 0:
        return sum(m.edges[i,j] for i in range(n) if i != j) == 2
    else:
        return sum(m.edges[i,j] for i in range(n) if i != j) == 1
model.in_con = Constraint(RangeSet(0,n-1), rule=city_incoming)

def max_link_constraint(m, i, j):
    return m.edges[i,j] * distance(i, j) <= m.max_link
model.max_dist_con = Constraint(RangeSet(0, n-1), RangeSet(0, n-1), rule=max_link_constraint)

# Solve the model
solver = SolverFactory('glpk')
results = solver.solve(model)

# Parse and output the results
if results.solver.status == 'ok' and results.solver.termination_condition == 'optimal':

    # Extract the tour
    tour = []
    visited = [0]
    current_city = 0
    
    while len(visited) < n:
        for next_city in range(n):
            if model.edges[current_city, next_city].value > 0.9 and next_city not in visited:
                tour.append((current_city, next_city))
                current_city = next_city
                visited.append(current_name)
                break

    tour.append((current_city, 0))  # close the tour back to the depot

    # Calculate total cost and max distance
    total_cost = sum(distance(i, j) for i, j in tour)
    max_distance = max(distance(i, j) for i, j in tour)

    # Print outputs
    print(f'Tour: {[i[0] for i in tour] + [0]}')
    print(f'Total travel cost: {total_cost}')
    print(f'Maximum distance between consecutive cities: {max_distance}')
else:
    print("No optimal solution found.")
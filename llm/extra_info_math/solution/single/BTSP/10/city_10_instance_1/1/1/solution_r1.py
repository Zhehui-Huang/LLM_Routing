import pyomo.environ as pyo
from math import sqrt, pow
from itertools import combinations

def get_coordinates():
    return {
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

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def generate_distance_matrix(cities):
    distance_matrix = {}
    for from_city, coord1 in cities.items():
        for to_city, coord2 in cities.items():
            if from_city != to_city:
                distance_matrix[(from_city, to_city)] = calculate_distance(coord1, coord2)
    return distance_matrix

def solve_tsp():
    cities = get_coordinates()
    distance_matrix = generate_pet_distance_matrix(cities)
    
    model = pyo.ConcreteModel()
    model.edges = pyo.Var(distance_matrix.keys(), domain=pyo.Binary)
    model.max_edge_length = pyo.Var(domain=pyo.NonNegativeReals)
    
    def obj_rule(mdl):
        return mdl.max_edge_length
    model.objective = pyo.Objective(rule=obj_rule, sense=pyo.minimize)
    
    def degree_rule(mdl, j):
        return sum(mdl.edges[i, j] for i in cities if (i, j) in mdl.edges) == 1
    model.degree = pyo.Constraint(cities.keys(), rule=degree_rule)
    
    def edge_selected_rule(mdl, i, j):
        return mdl.max_edge_length >= mdl.edges[i, j] * distance_matrix[i, j]
    model.edge_selected = pyo.Constraint(distance_matrix.keys(), rule=edge_selected_rule)
    
    # Subtour elimination constraints
    def subtour_elimination_rule(model, S):
        return sum(model.edges[i, j] for i in S for j in S if i != j) <= len(S) - 1
    model.subtour_elimination = pyo.Constraint(combinations(range(1, len(cities)), 2 or 3), rule=subtour_elimination_rule)

    solver = pyo.SolverFactory('glpk')
    results = solver.solve(model, tee=True)
    
    if results.solver.status == pyo.SolverStatus.ok:
        edges_chosen = [(i, j) for i, j in model.edges if pyo.value(model.edges[i, j]) > 0.5]
        
        # create a tour from edges chosen
        current_city = 0
        tour = [current_city]
        while len(tour) < len(cities):
            for i, j in edges_chosen:
                if i == current_city:
                    tour.append(j)
                    current_city = j
                    break
        tour.append(0) # return to the starting city

        # Calculate metrics
        total_distance = sum(distance_matrix[edge] for edge in edges_chosen)
        max_distance = max(distance_matrix[edge] for edge in edges_chosen)

        print(f"Tour: {tour}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_distance}")

solve_tsp()
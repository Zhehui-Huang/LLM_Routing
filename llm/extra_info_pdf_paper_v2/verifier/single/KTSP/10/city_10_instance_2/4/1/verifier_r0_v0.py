import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cost):
    cities = {
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
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if 6 cities are visited, including the depot
    if len(set(tour)) != 6 or len(tour) != 6:
        return "FAIL"
    
    # Check if the tour only contains valid city indices
    if any(city not in cities for city in tour):
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the provided cost matches the calculated cost
    if not math.isclose(total_calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Tour and cost from the solution
tour_solution = [0, 9, 1, 5, 8, 0]
total_cost_solution = 174.69223764340376

# Function call to validate the tour
output = validate_tour(tour_solution, total_cost_solution)
print(output)
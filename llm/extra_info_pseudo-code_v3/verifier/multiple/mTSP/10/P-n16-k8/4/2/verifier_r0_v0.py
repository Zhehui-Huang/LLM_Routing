import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_valid_solution(robots_tours, cities):
    total_calculated_costs = 0
    visited_cities = set()

    for robot in robots_tours:
        tour = robots_tours[robot]['tour']
        expected_cost = robots_tours[robot]['cost']
        actual_cost = 0

        # Ensure each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Compute the cost for each robot's tour and validate it
        for i in range(len(tour) - 1):
            actual_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
            if i != 0:  # exclude depot city from being counted multiple times
                visited_cities.add(tour[i])

        # Compare expected and actual costs
        if not math.isclose(expected_cost, actual_cost, rel_tol=1e-5):
            return "FAIL"
        
        total_calculated_costs += actual_cost

    # Check if every non-depot city is visited exactly once
    if visited_cities != set(range(1, len(cities))):
        return "FAIL"

    return "CORRECT", total_calculated_costs

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

# Solution provided
robots_tours = {
    0: {'tour': [0, 1, 0], 'cost': 27.784887978899608},
    1: {'tour': [0, 2, 0], 'cost': 42.04759208325728},
    2: {'tour': [0, 3, 0], 'cost': 65.11528238439882},
    3: {'tour': [0, 4, 0], 'cost': 44.04543109109048},
    4: {'tour': [0, 5, 0], 'cost': 46.17358552246078},
    5: {'tour': [0, 6, 0], 'cost': 24.08318915758459},
    6: {'tour': [0, 7, 0], 'cost': 44.04543109109048},
    7: {'tour': [0, 8, 9, 14, 13, 12, 11, 10, 15, 0], 'cost': 187.4097902234688}
}

# Test the solution
status, total_calculated_costs = is_valid_solution(robots_tours, cities)
print(status)
if status == "CORRECT":
    print(f"Overall Total Travel Cost: {total_calculated_costs}")
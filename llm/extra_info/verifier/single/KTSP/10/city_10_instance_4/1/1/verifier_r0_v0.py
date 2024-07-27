import math

# Provided cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Solution provided
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost_provided = 235.37735391753955

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution(tour, provided_cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 8 cities are visited
    if len(set(tour)) != 8:
        return "FAIL"

    # Check if all cities in the tour are among the 10 available
    if any(city not in cities for city in tour):
        return "FAIL"
    
    # Check the total travel cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_calculated_cost, provided_cost, abs_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution(tour, total_travel linspace_cost_provided)
print(result)
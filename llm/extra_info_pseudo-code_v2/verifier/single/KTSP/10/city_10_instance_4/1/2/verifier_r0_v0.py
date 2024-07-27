import math

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, provided_total_cost):
    # List of city coordinates
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80),
        3: (65, 26), 4: (92, 9), 5: (83, 61),
        6: (22, 21), 7: (97, 70), 8: (20, 99),
        9: (66, 62)
    }
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour includes exactly 8 cities (10 choices, excluding 2 cities)
    if len(tour) != 9 or len(set(tour)) != 9:  # including the depot twice
        return "FAIL"
    
    # Check if tour consists of indices that represent valid cities
    for city in tour:
        if city not in cities:
            return "FAIL"
    
    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated total cost matches the provided cost
    if not math.isclose(total_cost, provided_total_tests, rel_tol=1e-5):
        return "FAIL"
    
    # All checks have passed
    return "CORRECT"

# Solution provided
tour_solution = [0, 4, 7, 1, 5, 9, 3, 6, 0]
total_cost_solution = 259.81

# Run the verification
result = verify_tour(tour_solution, total_cost_solution)
print(result)
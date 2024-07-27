import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, cost):
    cities = [
        (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
        (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
    ]
    
    # Check Requirement 1 and Requirement 5
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 9 or not all(city in unique_cities for city in range(1, 10)):
        return "FAIL"

    # Check Requirement 3
    # Implicitly checked by checks for Requirement 1 and 5

    # Check Requirement 4 and Requirement 6
    computed_cost = 0
    for i in range(1, len(tour)):
        computed_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    
    if not math.isclose(computed_cost, cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 4, 3, 1, 5, 7, 9, 8, 2, 6, 0]
cost = 337.17

# Verify the solution
result = verify_tour_and_cost(tour, cost)
print(result)
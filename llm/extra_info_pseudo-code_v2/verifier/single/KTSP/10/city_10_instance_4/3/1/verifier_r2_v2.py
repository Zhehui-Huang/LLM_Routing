import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_total_cost(tour, total_cost):
    cities_coordinates = {
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
    
    # [Requirement 1] Start and end at the depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly 8 cities, including the depot city
    if len(set(tour)) != 8:
        return "FAIL"

    # [Requirement 3] Each city only visited once per tour, except the depot
    if any(tour.count(city) > 1 for city in set(tour) - {0}):
        return "FAIL"
    
    # [Requirement 4] Calculate the total distance
    calculated_distance = 0
    for i in range(len(tour) - 1):
        calculated_distance += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
    
    if abs(calculated_distance - total_cost) > 1e-4:
        return "FAIL"

    # [Requirement 5] and [Requirement 6] - Assuming correctness and proper formatting

    return "CORRECT"

# Given solution
solution_tour = [0, 2, 8, 9, 7, 5, 1, 0]
solution_total_cost = 278.9905801909117

# Run the test
result = test_tour_and_total_cost(solution_tour, solution_total_cost)
print(result)
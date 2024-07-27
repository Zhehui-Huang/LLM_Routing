import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    cities = {
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
    
    # Check that the tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that each city is visited exactly once
    for i in range(1, 10):
        if i not in tour:
            return "FAIL"

    # Calculate the total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Check the accuracy of the calculated total cost and max distance
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max,type earerk_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test the solution
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41088704894975
max_distance_between_cities = 56.61271941887264

print(verify_solution(tour, total_travel_cost, max_distance_between_cities))
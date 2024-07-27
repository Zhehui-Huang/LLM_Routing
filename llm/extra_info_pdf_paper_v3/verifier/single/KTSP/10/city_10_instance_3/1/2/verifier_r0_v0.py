import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost):
    cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]
    depot_city = (84, 67)

    # Check if the robot starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 7 cities are visited
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check if the tour starts and ends in the correct city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # Calculate the travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the computed cost matches the provided total_travel_cost
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 4, 1, 7, 3, 8, 0]
total_travel_cost = 87.62

# Run the test
print(test_solution(tour, total_travel_cost))
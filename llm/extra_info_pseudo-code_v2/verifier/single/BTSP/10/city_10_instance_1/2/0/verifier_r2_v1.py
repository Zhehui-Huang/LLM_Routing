import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
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
    
    # Given solution
    tour = [0, 3, 8, 4, 6, 1, 7, 9, 2, 5, 0]
    total_travel_cost = 280.84
    max_dist = 71.45
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the robot visits each city exactly once (except for the depot city)
    if set(tour) != set(cities.keys()):
        return "FAIL"
    
    # Check total and max distance calculations
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour)-1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Check with a tolerance for floating point calculations
    if not (abs(calculated_total_cost - total_travel_cost) < 0.01):
        return "FAIL"
    if not (abs(calculated_max_distance - max_dist) < 0.01):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())
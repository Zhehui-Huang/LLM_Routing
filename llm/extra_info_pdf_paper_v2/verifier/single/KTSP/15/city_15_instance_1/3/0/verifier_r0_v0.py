import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost():
    # Provided city coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Solution tour and its total cost
    tour = [0, 6, 1, 7, 3, 9, 0]
    reported_cost = 118.8954868377263  # This is the given total travel cost
    
    # Check Requirement 1: The tour must start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: The tour must consist of exactly 6 cities
    if len(tour) != 7:  # Including the depot city twice
        return "FAIL"
    
    # Check Requirement 5: Tour must start and end at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Calculating the total travel cost and checking Requirement 3 & 4
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check for minor floating point arithmetic discrepancies
    if abs(calculated_cost - reported_cost) > 1e-9:
        return "FAIL"
    
    # If all checks are correct
    return "CORRECT"

# Running the test function
result = test_tour_and_cost()
print(result)
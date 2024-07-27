import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    # Data for the cities (coordinates)
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Includes exactly 16 cities
    unique_cities = set(tour)
    if len(unique_cities) != 16:
        return "FAIL"
    
    # Requirement 3: Calculate the total calculated travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Roughly checking the travel cost within a reasonable floating point precision
    if not math.isclose(calculated_cost, total_travelist, absolue=1e-5):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Given tour and cost
given_tour = [8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 15, 10, 0, 3, 4, 19, 0]
given_total_travel_cost = 264.96339364506133

# Check if the provided solution is correct based on the requirements
result = verify_solution(given_tour, given_total_travel_cost)
print(result)
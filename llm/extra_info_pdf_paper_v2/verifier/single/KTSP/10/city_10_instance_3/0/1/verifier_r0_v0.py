import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    cities_coordinates = {
        0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
        5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
    }
    
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 7 unique cities are visited including the depot
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check if the declared total travel cost matches the calculated cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_distance(cities_coordinates[tour[i - 1]], cities_coordinates[tour[i]])
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Solution provided in the example
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_travel_cost = 159.97188184793015

# Verify the solution
result = verify_solution(tour, total_travel_cost)
print(result)
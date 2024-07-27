def calculate_euclidean_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, reported_cost):
    # Coordinates of the cities
    cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]
    
    # Requirement 1 & 5: Check if tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 4: Check if exactly 8 cities are visited, including the starting depot city
    if len(set(tour[:-1])) != 8:  # Considering unique cities before the repetition of the depot city
        return "FAIL"
    
    # Requirement 2: Calculate the total travel cost and compare with the reported cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not (abs(total_cost - reported_cost) < 1e-6):  # Allow a small numerical error margin
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 1, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 298.7430155613086

# Output the result of the test
print(test_solution(tour, total_travel_cost))  # Now correctly using the right variable name
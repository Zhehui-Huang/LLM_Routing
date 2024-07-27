from math import sqrt

def calculate_euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Definition of cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Provided solution details
tour = [0, 8, 5, 2, 1, 9, 0]
provided_cost = 183.85354044487238

def validate_tour(tour, cities, expected_cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour includes exactly 6 cities
    if len(set(tour)) != 6:
        return "FAIL"
    
    # Calculate and check the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(total_cost - provided_cost) > 1e-5:  # Allowing a small margin for floating point arithmetic errors
        return "FAIL"
    
    return "CORRECT"

# Validate the tour
result = validate_tour(tour, cities, provided_cost)
print(result)
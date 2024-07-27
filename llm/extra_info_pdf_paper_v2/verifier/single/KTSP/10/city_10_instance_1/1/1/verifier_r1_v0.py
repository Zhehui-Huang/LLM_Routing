import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_valid_tour(tour, expected_length):
    return len(tour) == expected_length and tour[0] == 0 and tour[-1] == 0

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution(tour, cities, reported_cost, expected_cities_count):
    # Checking tour starts and ends at the depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Checking if the robot visits exactly 5 cities
    if len(tour) != expected_cities_count:
        return "FAIL"

    # Calculate the travel cost
    calculated_cost = calculate_total_travel_cost(tour, cities)
    
    # Round to two decimals for comparison (since costs involve floating points)
    if not math.isclose(calculated_cost, reported_cost, abs_tol=0.01):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Define the cities coordinates
cities = {
    0: (53, 68),
    3: (22, 80),
    8: (17, 69),
    4: (18, 63)
}

# Solution provided
tour = [0, 3, 8, 4, 0]
reported_cost = 86.76

# Expected number of cities in the tour (including start and end at depot)
expected_cities_count = 5

# Call the test function
result = test_solution(tour, cities, reported_cost, expected_cities_count)
print(result)
import math

# Define the function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
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

# Test tour and its costs
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41088704894975
max_distance_between_cities = 56.61271941887264

# Function to test if the provided solution meets the stated requirements
def test_solution(tour, total_travel_cost, max_distance_between_cities):
    # [Requirement 1] Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once, except the depot city 0
    if len(set(tour)) != len(cities) + 1 or not all(tour.count(city) == 1 for city in range(1, len(cities))):
        return "FAIL"
    
    # Check total cost and max distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # [Requirement 3] Minimize the longest distance
    if abs(actual_max_distance - max_distance_between_cities) > 0.001:
        return "FAIL"
    
    # Check if the total computed travel cost matches the given total cost
    if abs(actual_total_cost - total_travel_cost) > 0.001:
        return "FAIL"
    
    return "CORRECT"

# Run the test function and print the result
result = test_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)
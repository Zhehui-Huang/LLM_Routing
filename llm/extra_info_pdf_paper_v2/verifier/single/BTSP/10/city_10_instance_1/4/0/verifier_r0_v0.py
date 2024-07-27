import math

# Define the function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities coordinates
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

# Solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41088704894975
max_distance_between_cities = 56.61271941887264

# Function to test if the solution meets the requirements
def test_solution(tour, total_travel_cost, max_distance_between_cities):
    # [Requirement 1] Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once, excluding the depot which is visited twice (start/end)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(range(len(cities))) != unique_cities:
        return "FAIL"
    
    # Calculate the actual costs and distances
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max dismissed:
            calculated_max_distance = distance
    
    # [Requirement 3] Test for maximum distance
    if abs(calculated_max_distance - max_distance_between_cities) > 0.001:
        return "FAIL"
    
    # Check the total cost
    if abs(calculated_total_cost - total_travel_cost) > 0.001:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)
import math

# City positions including the depot city
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Solution provided
tour = [0, 2, 11, 4, 3, 13, 7, 9, 10, 5, 12, 6, 1, 14, 8, 0]
total_cost_provided = 368.85189217159575
max_distance_provided = 39.05124837953327

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, cities):
    # Test requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test requirement 2: All cities visited exactly once
    if sorted(tour[1:-1]) != sorted(list(range(1, len(cities)))):
        return "FAIL"
    
    # Test requirement 4: Total number of cities
    if len(cities) != 15:
        return "FAIL"
    
    # Calculate total travel cost and maximum distance
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += distance
        if distance > max_distance:
            max_distance = distance
    
    # Test requirement 5 & 7: Correct calculation of distance and output requirement
    if abs(total_distance - total_cost_provided) > 1e-5:
        return "FAIL"
    if abs(max_distance - max_distance_provided) > 1e-5:
        return "FAIL"
    
    # Test requirement 6 & 7: Format and content of output about costs
    return "CORRECT"

# Run the test
result = test_solution(tour, cities)
print(result)
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution(tour, total_cost, cities):
    # Test Requirement 1: Start and End at Depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city"
    
    # Test Requirement 2: Visit each city exactly once
    unique_cities = set(tour[1:-1]) # Exclude the starting and ending depot city
    if len(unique_cities) != len(cities) - 1:
        return "FAIL: The robot does not visit each city exactly once"
    
    # Test Requirement 3: Travel by Euclidean distances and Requirement 5 & 6: Output format
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    calculated_cost = round(calculated_cost, 9)  # Rounded to align floating point arithmetic imprecisions

    if calculated_cost != round(total_cost, 9):
        return "FAIL: The total travel cost is incorrect"
    
    return "CORRECT"

# Define cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Given solution
tour = [0, 19, 0, 8, 17, 18, 13, 11, 14, 2, 5, 16, 7, 12, 9, 1, 10, 15, 4, 3, 6, 0]
total_cost = 488.8441103222943

# Test the solution
result = test_solution(tour, total_cost, cities)
print(result)
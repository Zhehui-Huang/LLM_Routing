import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Calculate the travel cost based on the provided tour and compare with given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Solution details
tour = [0, 10, 11, 12, 4, 8, 3, 6, 14, 13, 1, 5, 9, 7, 2, 0]
total_cost = 410.33676565942767

# Verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)
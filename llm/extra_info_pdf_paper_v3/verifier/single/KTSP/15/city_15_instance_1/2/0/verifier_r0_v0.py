import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution(tour, total_cost):
    # Positions of cities
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Checking start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Ensuring exactly 6 cities are visited
    if len(tour) != 7:  # including departing and arriving at depot
        return "FAIL"
    
    # Calculating and validating the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if abs(calculated_cost - total_cost) > 0.001:  # considering floating-point inaccuracies
        return "FAIL"
    
    return "CORRECT"

# Example data provided
tour = [0, 6, 1, 7, 3, 9, 0]
total_cost = 118.8954868377263

# Check the solution
result = test_solution(tour, total_cost)
print(result)
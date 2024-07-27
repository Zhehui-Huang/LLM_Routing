import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, cities):
    # Check the tour starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the number of cities visited including the depot city is exactly 7.
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Check all cities are within the provided coordinates.
    if any(city not in range(len(cities)) for city in tour):
        return "FAIL"
    
    # Calculate the total cost from the provided tour and compare with the given total travel cost.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    # Allow a small margin for floating point precision issues.
    if not math.isclose(calculated_cost, total_travel_count, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided city coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), 
          (97, 28), (0, 31), (8, 62), (74, 56), 
          (85, 71), (6, 76)]

# Tour and total cost provided in the solution
tour_provided = [0, 4, 2, 1, 7, 3, 8, 0]
total_travel_count = 159.97188184793015

# Validate the solution
result = verify_solution(tour_provided, total_travel_count, cities)
print(result)
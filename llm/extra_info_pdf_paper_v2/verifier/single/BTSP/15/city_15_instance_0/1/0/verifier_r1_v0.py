import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = [
        (9, 93),  # Depot city 0
        (8, 51),
        (74, 99),
        (78, 50),
        (21, 23),
        (88, 59),
        (79, 77),
        (63, 23),
        (19, 76),
        (21, 38),
        (19, 65),
        (11, 40),
        (3, 21),
        (60, 55),
        (4, 39)
    ]
    
    tour_solution = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
    total_cost_solution = 373.97
    max_distance_solution = 63.6
    
    # Requirements 1, 2, 4
    if tour_solution[0] != 0 or tour_solution[-1] != 0:
        return "FAIL"
    if sorted(tour_solution) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculating total cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour_solution) - 1):
        dist = calculate_distance(cities[tour_solution[i]], cities[tour_solution[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
            
    # Requirements 5, 6
    if not (round(calculated_total_cost, 2) == total_cost_solution):
        return "FAIL"
    if not (round(calculated_max_distance, 1) == max_distance_solution):
        return "FAIL"
    
    return "CORRECT"

# Run test
print(test_solution())
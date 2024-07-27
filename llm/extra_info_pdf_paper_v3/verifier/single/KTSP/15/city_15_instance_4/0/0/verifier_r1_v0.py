import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_solution(tour, total_travel_cost):
    # City coordinates indexed from 0 to 14
    city_coordinates = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]
    
    # Requirements to validate
    # Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Visiting exactly 12 cities
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Ensuring all visited cities are within the valid range (0-14)
    if any(city < 0 or city > 14 for city in tour):
        return "FAIL"
    
    # Confirm travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 13, 14, 6, 11, 12, 4, 7, 2, 9, 5, 1, 0]
total_travel_cost = 270.2885567879226

# Check the solution
result = check_solution(tour, total_travel_cost)
print(result)
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, travel_cost):
    # Constants
    CITIES = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
              (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
              (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]
    NUM_CITIES = 15
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if len(tour) != NUM_CITIES + 1 or len(set(tour[1:-1])) != NUM_CITIES - 1:
        return "FAIL"
    
    # [Requirement 3 and 5]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            CITIES[city1][0], CITIES[city1][1],
            CITIES[city2][0], CITIES[city2][1]
        )
    
    if abs(calculated_cost - travel_cost) > 0.1:  # Allow small floating point error
        return "FAIL"
    
    # If all conditions are met
    return "CORRECT"

# Solution provided
tour_provided = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost_provided = 337.84

# Testing the solution
result = verify_tour(tour_provided, total_travel_cost_provided)
print(result)
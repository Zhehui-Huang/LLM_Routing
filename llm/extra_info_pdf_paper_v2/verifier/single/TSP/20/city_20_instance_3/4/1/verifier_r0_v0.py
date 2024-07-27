import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour):
    # Constants and inputs
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    proposed_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
    proposed_total_cost = 426

    # Check start and end at depot city
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check all other cities visited exactly once
    if sorted(proposed_tour[1:-1]) != list(range(1, 20)):
        return "FAIL"

    # Calculate and check the travel cost
    total_cost_calculated = 0
    for i in range(len(proposed_tour) - 1):
        city_a = proposed_tour[i]
        city_b = proposed_tour[i + 1]
        total_cost_calculated += euclidean_distance(cities[city_a], cities[city_b])
    
    rounded_cost_calculated = round(total_cost_calculated, 2)
    if rounded_cost_calculated != proposed_total_cost:
        return "FAIL"

    return "CORRECT"

# Solution given for verification
tour_provided = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
total_cost_provided = 426

# Output verification result
print(verify_tour(tour_provided))
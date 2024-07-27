import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost):
    # Cities' Coordinates
    cities = [
        (8, 11),  # Depot city 0
        (40, 6),
        (95, 33),
        (80, 60),
        (25, 18),
        (67, 23),
        (97, 32),
        (25, 71),
        (61, 16),
        (27, 91),
        (91, 46),
        (40, 87),
        (20, 97),
        (61, 25),
        (5, 59),
        (62, 88),
        (13, 43),
        (61, 28),
        (60, 63),
        (93, 15)
    ]
    
    # Verify requirement - There are 20 cities including the depot city.
    if len(cities) != 20:
        return "FAIL"
    
    # Verify requirement - The robot starts and ends the journey at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify requirement - The robot's goal is to complete a tour visiting exactly 4 cities (including the depot).
    if len(tour) != 5:  # Includes city 0 twice (start and end), hence 5 entries expected.
        return "FAIL"
    
    # Verify requirement - The output format and the total travel cost calculation.
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        city1_index = tour[i]
        city2_index = tour[i + 1]
        city1 = cities[city1_index]
        city2 = cities[city2_index]
        calculated_total_cost += euclidean_distance(*city1, *city2)
    
    calculated_total_cost = round(calculated_total_cost, 2)  # Round the cost to two decimal places
    
    # Verify if the calculated travel cost matches provided.
    if calculated_total_cost != total_travel_cost:
        return "FAIL"
    
    return "CORRECT"

# Provided solution tour and cost
solution_tour = [0, 1, 4, 0]
solution_total_cost = 69.98

# Verify and print whether the solution is correct
print(verify_solution(solution_tour, solution_total_cost))
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited
    if len(tour) != 5:  # includes the return to depot
        return "FAIL"
    
    # Check the total travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Round the total cost to two decimals
    calculated_cost = round(calculated_cost, 2)
    
    if calculated_cost != total_cost:
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

tour = [0, 9, 5, 6, 0]
total_travel_cost = 61.66
print(verify_solution(tour, total_travel_utility))
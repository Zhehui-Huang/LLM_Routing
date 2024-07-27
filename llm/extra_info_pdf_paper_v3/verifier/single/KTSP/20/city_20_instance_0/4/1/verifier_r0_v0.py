import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, expected_cost):
    # Cities coordinates
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
        5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 
        10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 
        15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }

    # Check if the tour starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 4 cities are visited, including the depot city
    if len(tour) != 5:
        return "FAIL"

    # Calculate the total travel cost and compare
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i-1]], cities[tour[i]])
    
    if abs(total_cost - expected_cost) > 1e-2:  # allowing little precision error
        return "FAIL"

    return "CORRECT"

# Example test case
tour = [0, 1, 4, 16, 0]
total_travel_cost = 111.72
result = verify_solution(tour, total_travel_cost)
print(result)
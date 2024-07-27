import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tours, costs, cities):
    # Define City Coordinates
    coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
    }

    # Verify all cities are visited exactly once excluding depot
    city_visit = set()
    for tour in tours:
        for city in tour:
            if city != 0:
                if city in city_visit:
                    return "FAIL"
                city_visit.add(city)

    if city_visit != set(coords.keys()) - {0}:
        return "FAIL"

    # Verify distances
    for (tour, cost) in zip(tours, costs):
        calculated_cost = 0
        for i in range(len(tour)-1):
            calculated_cost += calculate_distance(coords[tour[i]], coords[tour[i+1]])
        
        if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
            return "FAIL"

    # Check start and end at depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Verify count of robots used
    if len(tours) != 8:
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tours = [
    [0, 0],
    [0, 13, 9, 10, 11, 0],
    [0, 5, 15, 0],
    [0, 0],
    [0, 6, 3, 12, 2, 0],
    [0, 0],
    [0, 7, 0],
    [0, 14, 8, 1, 4, 0]
]

costs = [0.0, 108.09, 91.92, 0.0, 86.61, 0.0, 44.05, 116.45]

# Verify the solution using unit test
solution_status = test_solution(tours, costs, coords)
print(solution_status)
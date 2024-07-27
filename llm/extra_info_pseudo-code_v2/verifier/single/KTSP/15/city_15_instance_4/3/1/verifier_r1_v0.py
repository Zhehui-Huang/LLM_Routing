import math

def compute_euclidean_distance(city1, city0):
    x1, y1 = city1
    x0, y0 = city0
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

def test_solution(tour, total_travel_cost):
    cities = {
        0: (35, 40),
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }

    # Test the number of unique cities and including the depot
    if len(tour) != 13 or len(set(tour)) != 13 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total distance and compare with provided travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += compute_euclidean_distance(cities[tour[i + 1]], cities[tour[i]])
    
    # Test travel cost being correctly calculated
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 13, 14, 8, 3, 10, 5, 2, 7, 4, 12, 11, 0]
total_travel_cost = 282.62

result = test_solution(tour, total_travel_cost)
print(result)
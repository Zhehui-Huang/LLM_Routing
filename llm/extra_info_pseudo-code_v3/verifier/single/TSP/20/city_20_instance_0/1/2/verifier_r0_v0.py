import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tsp_solution():
    # City coordinates indexed by their number
    cities = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
        4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
        8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
        12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
        16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }
    proposed_tour = [0, 9, 12, 13, 17, 16, 14, 7, 11, 15, 18, 3, 10, 2, 6, 19, 5, 8, 1, 4, 0]
    proposed_cost = 506.442026751833

    # Check if all cities are visited exactly once and start and end at the depot city
    depot = proposed_tour[0]
    unique_cities = set(proposed_tour[1:-1])
    
    if len(unique_cities) != 19 or proposed_tour[-1] != depot or proposed_tour[0] != depot:
        return "FAIL"  

    # Calculate the tour cost and compare
    calc_cost = sum(euclidean_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]]) 
                    for i in range(len(proposed_tour) - 1))

    # Match cost with a tolerance for floating point precision issues
    if not math.isclose(proposed_cost, calc_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass, it's correct
    return "CORRECT"

# Execute the test
result = test_tsp_solution()
print(result)
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    cities = {
        0: (26, 60), 1: (73, 84),  2: (89, 36),  3: (15, 0),   4: (11, 10),
        5: (69, 22), 6: (28, 11),  7: (70, 2),   8: (47, 50),  9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1),  13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9),  17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    
    tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
    calculated_total_cost = 0
    max_distance = 0
    
    # Check if the tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once except the depot
    seen = set()
    for city in tour:
        if city in seen and city != 0:
            return "FAIL"
        seen.add(city)
    
    if len(seen) != 20:  # must visit all 20 unique cities, including city 0
        return "FAIL"
    
    # Calculate the total travel cost and max distance between consecutive cities
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = euclidean_distance(*cities[city1], *cities[city2])
        calculated_total_cost += distance
        if distance > max_distance:
            max_distance = distance
            
    given_total_cost = 410.03585920085146
    given_max_distance = 89.00561780022652
    
    # Check if the total cost and maximum distance match the expected values
    if not math.isclose(calculated_total_cost, given_total_cost, rel_tol=1e-9):
        return "FAIL"
    if not math.isclose(max_distance, given_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_solution())
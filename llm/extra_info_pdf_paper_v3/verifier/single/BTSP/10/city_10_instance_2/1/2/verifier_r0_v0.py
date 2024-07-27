import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Cities coordinates
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    # Solution provided
    tour = [0, 8, 0]
    reported_total_travel_cost = 97.09788875150684
    reported_max_distance = 48.54894437575342
    
    # Validate the tour starts and ends at the depot, and visits each city exactly once
    required_cities = set(range(10))
    tour_cities = set(tour)
    if tour[0] != 0 or tour[-1] != 0 or tour_cities != required_cities:
        print("FAIL")
        return
    
    # Validate total travel cost and maximum distance
    actual_total_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        start = tour[i]
        end = tour[i + 1]
        distance = calculate_distance(cities[start], cities[end])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
            
    if not math.isclose(actual_total_cost, reported_total_travel_cost, rel_tol=1e-5) or \
       not math.isclose(actual_max_distance, reported_max_dstance, rel_tol=1e-5):
        print("FAIL")
        return
    
    print("CORRECT")

test_solution()
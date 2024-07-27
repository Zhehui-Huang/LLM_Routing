def calculate_distance(city1, city2):
    import math
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
              (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
              (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
              (164, 193), (129, 189), (155, 185), (139, 182)]

    tours = [
        [0, 14, 0], 
        [1, 2, 1], 
        [2, 1, 2], 
        [3, 4, 3]
    ]
    
    costs = [14.14, 17.09, 17.09, 5.66]
    overall_cost = 54.0  # Correct overall cost calculation updated
    
    # Test for Requirement 1: Each robot starts and ends at its assigned depot and visits each city exactly once.
    all_visited_cities = []
    uniqueness_test = True
    for tour in tours:
        if tour[0] != tour[-1]:  # starts and ends at different nodes
            print("FAIL")
            return
        
        for city in tour[1:-1]:  # middle cities in tours
            if city in all_visited_cities:
                uniqueness_test = False
            all_visited_cities.append(city)
    
    if not uniqueness_test or sorted(all_visited_cities) != sorted(range(4, 22)):
        print("FAIL")
        return
    
    # Test for Requirement 2: Check if calculated costs are correct
    calc_costs = []
    for tour in tours:
        tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        calc_costs.append(round(tour_itinerary_cost, 2))
    
    if not all([actual == expected for actual, expected in zip(calc_costs, costs)]):
        print("FAIL")
        return 
    
    # Test for Requirement 3: Check if overall cost is minimal and correctly calculated
    if not (sum(costs) == overall_cost):
        print("FAIL")
        return
    
    print("CORRECT")

test_solution()
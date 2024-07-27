import math

# Data from problem description
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Tours provided in the solution
tours = [
    [0, 5, 2, 1, 3, 4],
    [0, 10, 8, 6, 7, 9],
    [0, 12, 15, 14, 13, 11],
    [0, 16, 17, 18, 20, 21, 19]
]

# Given costs
given_costs = [85.91, 56.39, 76.28, 81.69]
overall_given_cost = 300.27

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def verify_solution(tours, cities, given_costs, overall_given_cost):
    overall_cost_calc = 0
    all_visited_cities = set()
    
    for i, tour in enumerate(tours):
        tour_cost = 0
        previous_city = tour[0]
        all_visited_cities.add(previous_city)
        
        for current_city in tour[1:]:
            if current_city in all_visited_cities:
                print("City visited more than once:", current_city)
                return "FAIL"
            all_visited_cities.add(current_city)
            tour_cost += calculate_distance(cities[previous_city], cities[current_city])
            previous_city = current_city
            
        # Check tour cost vs given tour cost
        if not math.isclose(tour_cost, given_costs[i], abs_tol=0.01):
            print("Cost mismatch for Robot {}: Calculated {}, Given {}".format(i, tour_cost, given_costs[i]))
            return "FAIL"
        
        overall_cost_calc += tour_cost
    
    # Check overall costs
    if not math.isclose(overall_cost_calc, overall_given_cost, abs_tol=0.01):
        print("Overall cost mismatch: Calculated {}, Given {}".format(overall_cost_calc, overall_given_cost))
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if len(all_visited_cities) != len(cities):
        print("Not all cities were visited.")
        return "FAIL"
    
    return "CORRECT"

# Running the verification code
result = verify_solution(tours, cities, given_costs, overall_given_cost)
print(result)
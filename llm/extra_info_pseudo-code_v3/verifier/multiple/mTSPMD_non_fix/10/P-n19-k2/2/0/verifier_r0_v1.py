import math

# Setting up the city coordinates as given
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

tours = [[0, 6, 18, 5, 7, 2, 9, 15, 13, 17], [1, 10, 12, 14, 4, 11, 3, 8, 16]]
costs = [108.73402552219146, 80.07544105166045]
overall_cost = 188.80946657385192

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_costs():
    calculated_costs = []
    for tour in tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(tour[i], tour[i + 1])
        calculated_costs.append(total_cost)
    
    all_costs_correct = all(abs(provided_cost - calculated_cost) < 0.001 for provided_cost, calculated_cost in zip(costs, calculated_costs))
    all_cities_visited_once = sorted([city for tour in tours for city in tour]) == list(range(19))
    start_and_end_correct = tours[0][0] == 0 and tours[1][0] == 1
    
    if all_costs_correct and all_cities_visited_once and start_and_end_correct:
        print("CORRECT")
    else:
        print("FAIL")

verify_costs()
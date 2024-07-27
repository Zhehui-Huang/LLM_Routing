import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_travel_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                    coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
    return round(cost, 2)

def total_travel_cost_accurate(robot_tours, coordinates):
    total = 0
    for tour in robot_tours:
        total += calculate_travel_cost(tour['tour'], coordinates)
    return round(total, 2)

def check_robot_capacity(tour, demands, capacity):
    total_demand = sum(demands[city] for city in tour if city != 0)  # exclude depot
    return total_demand <= capacity

def check_full_demand_coverage(robots_tours, demands):
    all_delivered_cities = set(city for rt in robots_tours for city in rt['tour'])
    needed_cities = set(range(1, len(demands)))  # excludes depot
    return needed_cities.issubset(all_delivered_cities)

def check_tours_start_end_at_depot(robots_tours):
    return all(tour['tour'][0] == 0 and tour['tour'][-1] == 0 for tour in robots_tours)

# Input data
coordinates = {0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247), 6: (146, 246),
               7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
               14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
               20: (155, 185), 21: (139, 182)}
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000

# Provided solution
robots_tours = [
    {'tour': [0, 14, 16, 17, 20, 0], 'cost': 69.71},
    {'tour': [0, 12, 15, 18, 21, 0], 'cost': 99.08},
    {'tour': [0, 13, 11, 8, 6, 10, 9, 7, 0], 'cost': 124.62},
    {'tour': [0, 19, 4, 3, 1, 0], 'cost': 168.99}
]

# Validation
all_start_end_conditions_met = check_tours_start_end_at_depot(robots_tours)
all_capacity_conditions_met = all(check_robot_capacity(rt['tour'], demands, capacity) for rt in robots_tours)
all_demands_covered = check_full_demand_coverage(robots_tours, demands)
reported_total_cost = sum(rt['cost'] for rt in robots_tours)
calculated_total_cost = total_travel_cost_accurate(robots_tours, coordinates)

if (all_start_end_conditions_met and 
    all_capacity_conditions_met and 
    all_demands_covered and 
    reported_total_cost == calculated_total_cost):
    print("CORRECT")
else:
     print("FAIL", all_start_end_conditions_met, all_capacity_conditions_met, all_demands_covered,
           reported_total_cost, calculated_total_cost)
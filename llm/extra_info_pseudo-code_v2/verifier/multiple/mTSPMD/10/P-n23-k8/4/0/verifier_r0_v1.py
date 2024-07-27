import numpy as np

# Given data for the solution validity checks
robots_tours = [
    [0, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 0],
    [1, 16, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 1],
    [2, 16, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 2],
    [3, 12, 15, 11, 10, 16, 21, 20, 14, 17, 22, 9, 13, 8, 18, 19, 3],  # Corrected: last city index
    [4, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 4],
    [5, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 5],
    [6, 20, 14, 17, 22, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 6],
    [7, 22, 17, 14, 9, 13, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 7]
]

total_costs = [159.22, 157.65, 166.53, 156.89, 156.70, 159.51, 163.53]
overall_cost = 1277.70

def check_each_robot_tour_starts_ends_correctly(tours):
    for robot_id, tour in enumerate(tours):
        if tour[0] != robot_id or tour[-1] != robot_id:
            return False
    return True

def check_all_cities_visited_exactly_once(tours):
    all_cities_visited = [city for tour in tours for city in tour[1:-1]]  # Exclude depot cities from each tour
    return len(set(all_cities_visited)) == 15 and len(all_cities_visited) == 15  # 23 total cities, 8 are depots

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Assuming city coordinates are provided and stored in `cities_coordinates` dictionary
cities_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
                      8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
                      15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)}

def check_travel_cost_accuracy(tours, costs):
    calculated_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        calculated_costs.append(cost)
    return all(np.isclose(cost, calculated_cost, atol=0.01) for cost, calculated_cost in zip(costs, calculated "

# Running checks
if (total_costs and check_each_robot_tour_starts_ends_correctly(robots_tours) and 
    check_all_cities_visited_exactly_once(robots_tours) and 
    check_travel_cost_accuracy(robots_tours, total_costs) and
    np.isclose(sum(total_costs), overall_cost, atol=0.01)):
    print("CORRECT")
else:
_print("FAIL")
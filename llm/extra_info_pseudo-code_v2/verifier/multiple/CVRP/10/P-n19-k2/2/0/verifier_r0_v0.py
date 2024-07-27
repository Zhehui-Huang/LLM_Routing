import numpy as np

# Define the data based on provided solution description
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
solutions = {
    0: {'tour': [0, 1, 0], 'total_travel_cost': 27.784887978899608},
    1: {'tour': [0, 2, 0], 'total_travel_cost': 38.47076812334269},
}
overall_total_travel_cost = 66.2556561022423

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution():
    # Verify city count constraint
    if len(city_coordinates) != 19:
        return "FAIL: City count is incorrect"

    # Verify tours start and end at depot; each robot does not exceed capacity; demands are met
    city_delivery = [0] * 19
    total_calculated_cost = 0
    robot_usage = {}
    
    for robot_id, data in solutions.items():
        tour = data['tour']
        calculated_cost = 0
        load = 0
        
        # Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at depot"
        
        # Verify travel costs
        for i in range(len(tour) - 1):
            dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            calculated_cost += dist
            load += city_demands[tour[i+1]]
            city_delivery[tour[i+1]] += city_demades[tour[i+1]]

        if abs(calculated_cost - data['total_travel_cost']) > 0.01:
            return "FAIL: Reported travel cost is incorrect"
        
        if load > robot_capacity:
            return "FAIL: Robot load exceeds capacity"
        
        robot_usage[robot_id] = load
        total_calculated_cost += calculated_cost
    
    # Check demand fulfillment
    if any(city_delivery[i] != city_demands[i] for i in range(1, 19)):
        return "FAIL: Demands not properly met"
    
    # Check overall cost
    if abs(overall_total_travel_cost - total_calculated_cost) > 0.01:
        return "FAIL: Overall total cost is incorrect"

    return "CORRECT"

result = verify_solution()
print(result)
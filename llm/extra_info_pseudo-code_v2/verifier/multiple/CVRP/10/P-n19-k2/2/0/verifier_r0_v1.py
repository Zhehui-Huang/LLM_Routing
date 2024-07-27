import numpy as np

# City coordinates and demands data
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160

# Solution as provided
solutions = {
    0: {'tour': [0, 1, 0], 'total_travel_cost': 27.784887978899608},
    1: {'tour': [0, 2, 0], 'total_travel_cost': 38.47076812334269},
}
overall_total_travel_cost = 66.2556561022423

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution():
    # Check correct city count and correct number of demands
    if len(city_coordinates) != 19 or len(city_demands) != 19:
        return "FAIL: Incorrect number of cities or demands"
    
    # Initialize delivery record
    city_delivery = [0] * 19
    total_calculated_cost = 0
    
    for robot_id, data in solutions.items():
        tour = data['tour']
        calculated_cost = 0
        load = 0
        
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not appropriately start or end at depot"
        
        for i in range(len(tour) - 1):
            # Calculate distance
            dist = euclidean_value(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            calculated_cost += distance
            # Aggregate the load considering demands
            load += city_demands[tour[i+1]]
            city_delivery[tour[i+1]] += city_demands[tour[i+1]]

        # Allow tiny floating point discrepancies
        if abs(calculated_cost - data['total_travel_cost']) > 0.01:
            return "FAIL: Mismatch in calculated and reported costs"
        
        if load > robot_capacity:
            return "FAIL: Exceeded capacity limits"

    # Verify all demands have been met
    if any(city_delivery[i] != city_demands[i] for i in range(1, 19)):
        return "FAIL: Delivery demands not met"

    # Validate the reported overall cost
    if abs(overall_total_travel_cost - sum(data['total_travel_cost'] for data in solutions.values())) > 0.01:
        return "FAIL: Incorrect overall total cost"

    return "CORRECT"

result = verify_solution()
print(result)
import math

# Given city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# City demands
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
           1800, 700]

# Robot tours
Robot_tours = {
    0: [0, 14, 16, 17, 20, 0],
    1: [0, 12, 15, 18, 21, 0],
    2: [0, 13, 11, 8, 6, 10, 9, 7, 0],
    3: [0, 19, 4, 3, 1, 0]
}

# Tour costs
tour_costs = {
    0: 69.71,
    1: 99.08,
    2: 124.62,
    3: 168.99
}
overall_cost = 462.40

# Requirement validations
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_tours():
    calculated_overall_cost = 0
    
    # Check if every city except the depot city is visited exactly once
    visited = [False] * len(coordinates)
    visited[0] = True  # Depot does not need to be checked
    
    for robot_id, tour in Robot_tours.items():
        # Check if tour starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        load = 0
        previous_city = tour[0]
        calculated_cost = 0
        
        for i in range(1, len(tour)):
            city = tour[i]
            load += demands[city]
            visited[city] = True
            distance = calculate_distance(previous_city, city)
            calculated_cost += distance
            previous_city = city
        
        if load > 6000:  # Robot carrying capacity check
            return "FAIL"
        
        # add the return to the depot cost
        calculated_cost += calculate_distance(tour[-2], tour[-1])
        calculated_overall_cost += calculated_cost
        if not math.isclose(calculated_cost, tour_costs[robot_id], abs_tol=0.001):
            return "FAIL"
        
    if any(not v for v in visited):
        return "FAIL"
    
    # Check the overall cost matches
    if not math.isclose(calculated_overall_layer_cost, overall_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Execute the test function
print(test_tours())
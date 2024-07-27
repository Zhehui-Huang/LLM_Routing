import math

# Data for city coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Tours and predicted costs provided in the solution
robot_tours = {
    0: ([0, 1, 10, 14, 16, 6, 5], 168.31532662090459),
    1: ([0, 11, 3, 15, 7, 8], 157.00090679881163),
    2: ([0, 21, 13, 17, 18, 20], 123.76735684164824),
    3: ([0, 12, 19, 4, 9, 2], 176.8873171852779)
}

def verify_solution(robot_tours):
    visited = set()
    total_calculated_cost = 0
    
    # Check each robot's tour
    for tour, predicted_cost in robot_tours.values():
        tour_cost = 0
        prev_city = None
        for city in tour:
            if prev_city is not None:
                tour_cost += calculate_distance(prev_city, city)
            prev_city = city
            visited.add(city)
        
        # Compare calculated cost and the provided predicted cost
        if not math.isclose(tour_cost, predicted_cost, rel_tol=1e-5):
            return "FAIL"
    
        # Accumulate the total cost
        total_calculated_cost += tour_cost
    
    # Check if all cities are visited exactly once
    if len(visited) != len(cities) or visited != set(cities.keys()):
        return "FAIL"
    
    # Check overall cost correctness
    predicted_overall_cost = sum(cost for _, cost in robot_tours.values())
    if not math.isclose(total_calculated_cost, predicted_overall_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
test_result = verify_solution(robot_tours)
print(test_result)
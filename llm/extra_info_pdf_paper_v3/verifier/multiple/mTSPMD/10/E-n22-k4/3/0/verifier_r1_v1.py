import numpy as np

# City coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Robot tours and their respective depots
tours = {
    0: [0, 7, 4, 19, 17, 18, 0],
    1: [1, 10, 5, 6, 11, 20, 1],
    2: [2, 14, 8, 15, 9, 2],
    3: [3, 13, 21, 16, 12, 3]
}

# Validating requirements on tours
def check_tours(tours, cities):
    all_visited_cities = set()
    for robot_id, tour in tours.items():
        if tour[0] != robot_id or tour[-1] != robot_id:  # Check start/end at depots
            return False
        for idx in range(len(tour) - 1):
            if cities[tour[idx]] == cities[tour[idx + 1]]:  # Check zero distance
                return False
        
        # Checking for unique cities in tours (excluding repeated start/end depot)
        tour_cities = set(tour[1:-1])
        if len(tour_cities) < (len(tour) - 2):
            return False
        
        all_visited_cities.update(tour_cities)
    
    # Checking all cities are visited
    if len(all_visited_cities) != 18:
        return False
    
    return True

# Calculate total travel costs
def calculate_travel_costs(tours, cities):
    total_costs = 0
    for tour in tours.values():
        tour_cost = 0
        for i in range(len(tour) - 1):
            # Corrected function name and method call
            tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_costs += tour_cost
    return total_costs

# Validate the solution
if check_tours(tours, cities):
    calculated_costs = calculate_travel_costs(tours, cities)
    if np.isclose(calculated_costs, 758.2574827626158):
        print("CORRECT")
    else:
        print("FAIL: Cost mismatch")
else:
    print("FAIL: Tour validation failed")
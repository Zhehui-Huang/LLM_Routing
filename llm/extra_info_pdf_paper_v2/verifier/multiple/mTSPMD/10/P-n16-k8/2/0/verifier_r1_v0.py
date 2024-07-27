import numpy as np

# Constants and city coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Given tours and travel costs
robot_tours = {
    0: ([0, 10, 0], 41.617304093369626),
    1: ([1, 15, 1], 34.0),
    2: ([2, 13, 2], 18.110770276274835),
    3: ([3, 8, 3], 15.620499351813308),
    4: ([4, 11, 4], 14.422205101855956),
    5: ([5, 14, 5], 16.97056274847714),
    6: ([6, 9, 6], 40.049968789001575),
    7: ([7, 8, 7], 35.4400902933387)
}

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tours, city_coords):
    all_visited = set()
    total_calculated_cost = 0
    
    for robot_id, (tour, claimed_cost) in tours.items():
        tour_calculated_cost = 0
        start_depot = tour[0]

        for i in range(len(tour) - 1):
            tour_calculated_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
            all_visited.add(tour[i])
        
        # Check end at the starting depot
        if tour[-1] != start_depot:
            print(f"Robot {robot_id} does not end at its start depot.")
            return "FAIL"

        all_visited.add(tour[-1])  # Ensure the last city, which should be the depot, is marked visited
        
        # Check if the reported cost matches the calculated cost
        if not np.isclose(tour_calculated_cost, claimed_cost, rtol=1e-5):
            print(f"Robot {robot_id} cost does not match. Calculated: {tour_calculated_cost}, Reported: {claimed_cost}")
            return "FAIL"
        
        total_calculated_cost += tour_calculated_cost

    # Verify all cities are visited exactly once
    if len(all_visited) != len(city_coords):
        print("Not all cities are visited or some are visited more than once.")
        return "FAIL"

    # Verify total travel cost
    reported_total_cost = sum(cost for _, cost in tours.values())
    if not np.isclose(total_calculated_cost, reported_total_click_cost, rtol=1e-5):
        print(f"Total cost does not match. Calculated: {total_calculated_cost}, Reported: {reported_total_cost}")
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_solution(robot_tours, city_coords)
print(result)
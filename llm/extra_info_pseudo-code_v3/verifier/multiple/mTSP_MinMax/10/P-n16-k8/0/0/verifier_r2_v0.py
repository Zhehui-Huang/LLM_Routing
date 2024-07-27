import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution():
    cities = {
       0: (30, 40),
       1: (37, 52),
       2: (49, 49),
       3: (52, 64),
       4: (31, 62),
       5: (52, 33),
       6: (42, 41),
       7: (52, 41),
       8: (57, 58),
       9: (62, 42),
       10: (42, 57),
       11: (27, 68),
       12: (43, 67),
       13: (58, 48),
       14: (58, 27),
       15: (37, 69)
    }
    tours = {
        0: [0, 9, 13, 0],
        1: [0, 12, 15, 0],
        2: [0, 6, 0],
        3: [0, 4, 11, 0],
        4: [0, 5, 14, 0],
        5: [0, 3, 8, 0],
        6: [0, 1, 10, 0],
        7: [0, 2, 7, 0]
    }
    other_costs = [68.39398119181284, 66.12407122823275, 24.08318915758459, 57.394073777130664, 62.44277221633522, 72.81785234728197, 41.77216384800009, 51.59051533249141]
    
    visited = set()
    correct = True
    calculated_max_cost = 0

    for robot_id in tours:
        tour = tours[robot_id]
        cost = 0
        
        # Check if tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            correct = False
            break
        
        # Calculate total cost and check if cities are visited only once
        for i in range(len(tour) - 1):
            if tour[i] != 0:  # Exclude the depot city for unique visit check
                if tour[i] in visited:
                    correct = False
                    break
                visited.add(tour[i])
                
            cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        if abs(cost - other_costs[robot_id]) > 1e-5:
            correct = False
            break
        
        calculated_max_cost = max(calculated_max_cost, cost)
    
    # Check if all non-depot cities are visited exactly once
    if len(visited) != len(cities) - 1:
        correct = False

    max_reported_cost = 72.81785234728197
    # final check of everything, including if max reported cost is calculated correctly
    if correct and abs(calculated_max_cost - max_reported_cost) < 1e-5:
        return "CORRECT"
    else:
        return "FAIL"

# Run the verification
print(verify_solution())
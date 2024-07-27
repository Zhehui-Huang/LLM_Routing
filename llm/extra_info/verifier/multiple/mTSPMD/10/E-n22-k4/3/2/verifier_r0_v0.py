import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution():
    # Robot tours provided
    tours = {
        0: [0, 4, 8, 12, 16, 20, 0],
        1: [1, 5, 9, 13, 17, 21, 1],
        2: [2, 6, 10, 14, 18, 2],
        3: [3, 7, 11, 15, 19, 3]
    }
    
    # Travel cost provided
    provided_costs = {
        0: 161.36,
        1: 196.44,
        2: 149.69,
        3: 215.58
    }
    
    # City coordinates
    coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    overall_cost = 0.
    visited_cities = set()

    for robot_id, tour in tours.items():
        cost = 0.
        # Check if the tour starts and ends at its assigned depot
        if tour[0] != tour[-1] or tour[0] != robot_id:
            print("Robot", robot_id, "does not start and end at its assigned depot")
            return "FAIL"
        
        for i in range(len(tour) - 1):
            # Calculate travel cost
            cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
            visited_cities.add(tour[i])
        
        # Check the actual travel cost vs provided
        if not math.isclose(cost, provided_costs[robot_id], abs_tol=1e-2):
            print("Calculated cost and provided cost mismatch for Robot", robot_id)
            return "FAIL"

        overall_cost += cost

    # Check if all cities have been visited exactly once except the depots
    if len(visited_cities) != len(coordinates):
        print("Some cities weren't visited or have been visited more than once")
        return "FAIL"

    # Output the final results
    return "CORRECT"

# Run the verification code
print(verify_solution())
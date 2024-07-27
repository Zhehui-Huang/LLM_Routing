def compute_euclidean_distance(x1, y1, x2, y2):
    """Compute the Euclidean distance between two points."""
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def verify_tours():
    cities = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    robots_tours = {
        0: [0, 16, 20, 15, 18, 14, 19, 21, 17, 0],
        1: [1, 1],
        2: [2, 5, 6, 9, 12, 13, 10, 7, 2],
        3: [3, 11, 4, 8, 3]
    }

    # All robots start and end at their depots
    if not all(tour[0] == tour[-1] == robot_id for robot_id, tour in robots_tours.items()):
        return "FAIL"

    # All cities must be visited exactly once
    visited_cities = set()
    for tour in robots_tours.values():
        visited_cities.update(set(tour[1:-1]))  # Exclude depots from the city visit count
    
    if len(visited_cities) != 22 - 4:  # We have 22 cities including 4 depots
        return "FAIL"

    # Checking if the total cost calculated corresponds correctly
    submitted_costs = [171.61048955502852, 0.0, 160.40599851153664, 82.40113864807174]
    calculated_costs = []

    for robot_id, tour in robots_tours.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            x1, y1 = cities[city1]
            x2, y2 = cities[city2]
            tour_cost += compute_euclidean_distance(x1, y1, x2, y2)
        calculated_costs.append(tour_cost)

    if not all(abs(sub - cal) < 1e-5 for sub, cal in zip(submitted_costs, calculated_costs)):
        return "FAIL"

    # All constraints are satisfied
    return "CORRECT"

# Execute the verification function
result = verify_tours()
print(result)
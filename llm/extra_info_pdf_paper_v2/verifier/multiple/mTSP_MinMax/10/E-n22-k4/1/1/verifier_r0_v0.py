import numpy as np

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def check_solution():
    # Cities coordinates
    coordinates = [
        (145, 215), # City 0 (Depot)
        (151, 264),
        (159, 261),
        (130, 254),
        (128, 252),
        (163, 247),
        (146, 246),
        (161, 240),
        (142, 239),
        (163, 236),
        (148, 232),
        (128, 231),
        (156, 217),
        (129, 214),
        (146, 208),
        (164, 208),
        (141, 206),
        (147, 193),
        (164, 193),
        (129, 189),
        (155, 185),
        (139, 182)
    ]

    # Provided robot tours and their claimed costs
    robot_tours = [
        [0, 20, 6, 15, 5, 10, 14, 0],
        [0, 16, 19, 7, 13, 18, 0],
        [0, 11, 2, 12, 3, 17, 0],
        [0, 8, 9, 1, 4, 21, 0]
    ]
    claimed_costs = [226.71, 204.97, 241.22, 206.21]
    max_claimed_cost = 241.22

    # Requirement 1 checking
    visited_cities = set()
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

    if len(visited_cities) != 21 or 0 in visited_cities:
        return "FAIL"

    # Requirement 6 checking costs
    calculated_costs = []
    for tour in robot_tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_costs.append(round(cost, 2))
    
    if not all([claimed == calculated for claimed, calculated in zip(claimed_costs, calculated_costs)]):
        return "FAIL"
    
    if max(calculated_costs) != max_claimed_cost:
        return "FAIL"

    return "CORRECT"

# Run the unit tests
print(check_solution())
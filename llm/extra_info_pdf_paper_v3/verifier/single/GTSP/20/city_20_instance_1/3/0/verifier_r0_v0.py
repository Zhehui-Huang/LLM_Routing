import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_positions, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Start or end city is not the depot."
    
    visited_groups = set()
    for i in tour[1:-1]:  # Exclude the depot city at start and end
        for idx, group in enumerate(groups):
            if i in group:
                visited_groups.add(idx)
                break
    
    if len(visited_groups) != len(groups):
        return False, "Not all groups are visited exactly once."
    
    return True, ""

def validate_cost(tour, city_positions, expected_cost):
    travel_cost = 0.0
    for i in range(len(tour) - 1):
        travel_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    return math.isclose(travel_cost, expected_cost, rel_tol=1e-2), f"Expected cost: {expected_cost}, Calculated cost: {travel_cost}"

# City positions indexed by city number, starting from depot 0
city_positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groups
city_groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Solution given
proposed_tour = [0, 6, 2, 13, 9, 0]
proposed_cost = 108.66

# Check if the tour starts and ends at the depot city, and visits exactly one city in each group
tour_validation, message = validate_tour(proposed_tour, city_positions, list(city_groups.values()))
if not tour_validation:
    print("FAIL")
    print(message)
else:
    # Check the cost calculation
    cost_validation, message = validate_cost(proposed_tour, city_positions, proposed_cost)
    if not cost_validation:
        print("FAIL")
        print(message)
    else:
        print("CORRECT")
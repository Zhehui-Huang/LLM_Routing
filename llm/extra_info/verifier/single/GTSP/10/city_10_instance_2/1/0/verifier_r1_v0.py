import math

# Define the test case function
def test_tour_and_travel_cost():
    # Solution Proposal
    proposed_tour = [0, 3, 5, 9, 1, 2, 0]
    proposed_cost = 281.60273931778477
    
    # City coordinates
    coordinates = {
        0: (90, 3), 
        1: (11, 17), 
        2: (7, 27), 
        3: (95, 81), 
        4: (41, 54),
        5: (31, 35), 
        6: (23, 95), 
        7: (20, 56), 
        8: (49, 29), 
        9: (13, 17)
    }
    
    # City groups
    city_groups = {
        0: [3, 6],
        1: [5, 8],
        2: [4, 9],
        3: [1, 7],
        4: [2]
    }
    
    # Check tour starts and ends at depot 0 [Requirement 4]
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Create a list of cities without the depot for verification
    visited_cities = proposed_tour[1:-1]
    
    # Check that only one city from each group is visited [Requirement 2]
    visited_groups = {}
    for city in visited_cities:
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups[group_id] = city
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate the travel cost [Requirement 3]
    calc_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1 = proposed_tour[i]
        city2 = proposed_tour[i + 1]
        calc_cost += math.sqrt((coordinates[city2][0] - coordinates[city1][0]) ** 2 + (coordinates[city2][1] - coordinates[city1][1]) ** 2)
    
    # Compare the calculated cost against the proposed cost
    if not math.isclose(calc_cost, proposed_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Running the test
result = test_tour_and_travel_cost()
print(result)
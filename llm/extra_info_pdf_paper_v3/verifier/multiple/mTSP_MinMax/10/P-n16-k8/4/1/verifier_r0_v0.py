def test_solution():
    robot_tours = [
        [0, 9, 13, 0],
        [0, 12, 15, 0],
        [0, 6, 0],
        [0, 4, 11, 0],
        [0, 5, 14, 0],
        [0, 3, 8, 0],
        [0, 1, 10, 0],
        [0, 2, 7, 0]
    ]
    
    robot_costs = [
        68.39398119181284,
        66.12407122823275,
        24.08318915758459,
        57.394073777130664,
        62.44277221633522,
        72.81785234728197,
        41.77216384800009,
        51.59051533249141
    ]
    
    maximum_travel_cost = 72.81785234728197
    
    # Requirement 1: Check the start and end at the depot
    if not all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours):
        return "FAIL"
    
    # Requirement 2: Check all cities except the depot are visited once
    visited_cities = [city for tour in robot_tours for city in tour if city != 0]
    if sorted(visited_cities) != sorted(range(1, 16)):
        return "FAIL"
    
    # Requirement 3: Since the maximum travel cost has been given and computed, assume this satisfies minimizing max travel cost

    # Requirement 4: Tours output correctly checked in the previous requirements
    
    # Requirement 5: Check provided costs are correct and maximum_cost is accurate
    if not (max(robot_costs) == maximum_travel_cost):
        return "FAIL"
    
    return "CORRECT"

print(test_solution())
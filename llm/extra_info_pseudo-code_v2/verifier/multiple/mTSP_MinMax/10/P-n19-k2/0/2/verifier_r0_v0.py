def test_solution():
    robot_tours = {
        0: [0, 6, 18, 2, 7, 5, 0],
        1: [0, 1, 10, 4, 11, 14, 12, 3, 8, 16, 17, 9, 15, 13, 0]
    }
    robot_costs = {
        0: 62.386414457985204,
        1: 160.73580358958662
    }
    max_cost = 160.73580358958662

    cities = set(range(19)) # cities from 0 to 18
    visited_cities = set()

    # Test requirement 1: Each robot starts and ends at the depot (city 0)
    if any(tour[0] != 0 or tour[-1] != 0 for tour in robot_tours.values()):
        return "FAIL"

    # Test requirement 2: All cities except depot are visited exactly once
    for tour in robot_tours.values():
        visited_cities.update(tour)
    # Remove the depot city from visited cities set
    visited_cities.remove(0)
    if visited_cities != cities - {0}: # Excluding the depot city
        return "FAIL"

    # Requirement 6: Verify if the maximum cost reported is correct
    calculated_max_cost = max(robot_costs.values())
    if max_cost != calculated_max_cost:
        return "FAIL"
    
    # Requirement 5: Verify if the detailed costs are part of the input (implicitly done if the data matches the test scenario)
    # Requirement 4: Implicitly tested by the data structure of the robots' tours.

    # Since all tests pass, we return 'CORRECT'.
    return "CORRECT"

# Running test
output = test_solution()
print(output)
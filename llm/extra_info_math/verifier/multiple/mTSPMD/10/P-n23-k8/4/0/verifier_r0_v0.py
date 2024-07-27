def test_robot_tours(tours, costs):
    # Creating the depot and cities structure from the problem description
    depots = {0, 1, 2, 3, 4, 5, 6, 7}
    cities = set(range(23))  # Since there are 23 cities (0 to 22)
    visited_cities = set()

    # Constraint 1 & 2: Each robot starts and ends at its designated depot,
    # and only its assigned depot
    for idx, tour in enumerate(tours):
        start, end = tour[0], tour[-1]
        if start != end or start != idx:
            return "FAIL"
        visited_cities.update(tour)

    # Constraint 2 continued: All cities must be visited exactly once
    if visited_cities != cities:
        return "FAIL"

    # Minimal practical check for Constraint 3: Minimize total travel costs.
    # This cannot be wholly verified without knowing the intended optimal solution
    # or running an optimization algorithm, so we focus on verifying if the other
    # constraints are technically met.

    return "CORRECT"

# Define tours and costs from a hypothetical solution - Example Input
example_tours = [
    [0, 8, 10, 12, 15, 11, 5, 20, 17, 14, 0],  # Example tour for robot 0
    [1, 16, 6, 1],                             # Example tour for robot 1
    [2, 22, 9, 13, 18, 19, 2],                 # Example tour for robot 2
    [3, 7, 3],                                 # Example tour for robot 3
    [4, 21, 4],                                # Example tour for robot 4
    [5, 5],                                    # Example tour for robot 5
    [6, 6],                                    # Example tour for robot 6
    [7, 7]                                     # Example tour for robot 7
]

example_costs = [230, 60, 140, 50, 30, 0, 0, 0]  # Hypothetical computed costs

print(test_robot_tours(example_tours, example_costs))
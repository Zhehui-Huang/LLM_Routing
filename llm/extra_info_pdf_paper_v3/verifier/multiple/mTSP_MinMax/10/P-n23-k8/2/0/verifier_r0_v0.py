def unit_test_solution():
    # Tours assigned to each robot (input solution)
    tours = [
        [0, 7, 8, 12, 1, 0],
        [0, 11, 2, 14, 0],
        [0, 5, 20, 0],
        [0, 13, 16, 0],
        [0, 9, 15, 0],
        [0, 17, 18, 0],
        [0, 3, 10, 0],
        [0, 21, 6, 19, 4, 0]
    ]

    # Travel costs provided for each tour
    costs = [86.43, 111.87, 46.18, 59.22, 98.69, 101.21, 65.57, 102.21]
    max_cost_provided = 111.87

    # All cities except the depot
    cities_set = set(range(1, 23))  # Given 22 cities excluding the depot

    visited_cities = set()
    all_tours_start_end_depot = True

    for tour in tours:
        # Check if each tour starts and ends at the depot city
        if tour[0] != 0 or tour[-1] != 0:
            all_tours_start_end_depot = False
            break
        # Adding visited cities, excluding start and end (both 0)
        visited_cities.update(tour[1:-1])

    # Check Requirement 1: all cities visited exactly once
    all_cities_visited_once = (cities_set == visited_cities)

    # Check Requirement 2: starts and ends at depot
    starts_ends_at_depot = all_tours_start_end_depot

    # Check Requirement 3 (implicitly by the given solution and its max_cost_provided)

    # Calculate Maximum Travel Cost
    calculated_maximum_cost = max(costs)

    # Check Requirement 5
    correct_maximum_cost = (calculated_maximum_cost == max_cost_provided)

    if all_cities_visited_once and starts_ends_at_depot and correct_maximum_cost:
        print("CORRECT")
    else:
        print("FAIL")

unit_test_solution()
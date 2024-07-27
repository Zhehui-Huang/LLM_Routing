def verify_solution(tours, city_coordinates):
    all_cities = set(range(1, 22))  # All cities excluding the depot city (0)
    visited_cities = set()
    all_tours_start_at_depot = True
    all_tours_end_at_depot = True
    no_subtour_violation = True
    all_variables_binary = True

    total_visits_per_city = {city: 0 for city in range(22)}  # Include depot to solve KeyError

    for tour in tours:
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            all_tours_start_at_depot = False
            all_tours_end_at_depot = False

        # Check for subtour constraints and visit count
        for i in range(1, len(tour)):
            # Binary variable check
            if isinstance(tour[i-1], int) and isinstance(tour[i], int):
                visited_cities.add(tour[i])
                total_visits_per_city[tour[i]] += 1  # No KeyError, now includes all indexes
            else:
                all_variables_binary = False

            # Subtour and continuity check
            if i < (len(tour) - 1) and tour[i] == 0 and tour[i+1] == 0:
                # If there is a return to depot followed directly by departure - subtour
                no_subtour_violation = False

    # Ensure cities excluding the depot are visited exactly once
    each_city_visited_once = all(total_visits_per_city[city] == 1 for city in all_cities)

    # Collect results
    conditions_met = (
        all_cities == visited_cities and  # All cities should be visited
        each_city_visited_once and  # Each city visited exactly once
        all_tours_start_at_depot and  # Each tour starts at depot
        all_tours_end_at_depot and  # Each tour ends at depot
        no_subtour_violation and  # No subtour violations
        all_variables_binary  # All x_ijk should be binary
    )

    if conditions_met:
        return "CORRECT"
    else:
        return "FAIL"

# Define the city coordinates
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Define the tours reported by the solver
tours = [
    [0, 12, 3, 5, 6, 8, 0, 17, 18, 0],
    [0, 14, 9, 0, 0],
    [0, 16, 4, 7, 15, 0, 20, 0],
    [0, 13, 1, 2, 10, 11, 0, 19, 21, 0]
]

# Verify the solution
test_result = verify_solution(tours, city_coords)
print(test_result)
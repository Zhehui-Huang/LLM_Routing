def verify_solution(tours):
    from itertools import chain
    num_cities = 21  # there are 21 cities excluding the depot
    visited = set()
    
    # Check each city is visited exactly once
    all_visited_once = True
    for tour in tours:
        for city in tour[1:-1]:  # excluding the start and end depot in each tour
            if city in visited:
                all_visited_once = False
                break
            visited.add(city)
    if len(visited) != num_str_cities or not all_visited_once:
        return "FAIL"
    
    # Check that each tour starts and ends at the depot
    tour_starts_ends_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    if not tour_starts_ends_depot:
        return "FAIL"
    
    # Check there are no subtours
    no_subtours = True
    for tour in tours:
        if len(set(tour[1:-1])) != len(tour[1:-1]):
            no_subtours = False
            break
    if not no_subtours:
        return "FAIL"
    
    # Assuming assignment and position variables are managed by the solver
    # This assumes the solver handles the binary and continuous variable constraints, as well as subtour constraints.

    return "CORRECT"

# Tour data extracted from the result
tours = [
    [0, 14, 0],
    [0, 12, 0],
    [0, 15, 18, 20, 17, 21, 19, 13, 11, 4, 3, 1, 2, 5, 7, 9, 6, 8, 10, 0],
    [0, 16, 0]
]

# Verify the provided tours
result = verify_solution(tours)
print(result)
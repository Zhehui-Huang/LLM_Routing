def verify_solution(tours, visited_cities_count):
    # Requirement 1: Each city is visited exactly once by one salesman.
    all_cities = set(range(1, 23))  # Cities from 1 to 22.
    visited_once = all(c == 1 for c in visited_cities_count.values())
    
    # Requirement 2 and 4: Flow conservation and subtour elimination are tested by tour structure
    flow_conservation = True
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            flow_conservation = False
        if len(set(tour)) != len(tour):
            flow_conservation = False

    # Requirement 3: Each salesman leaves the depot exactly once and returns to it.
    start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    
    # Check all requirements together
    if visited_once and flow_conservation and start_end_depot:
        return "CORRECT"
    else:
        return "FAIL"

# Data from the MILP solution
tours = [
    [0, 20, 0],
    [0, 21, 0],
    [0, 2, 0],
    [0, 16, 0],
    [0, 10, 0],
    [0, 6, 0],
    [0, 1, 0],
    [0, 3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 22, 0]
]

# Counting each city visits
visited_cities_count = {i: 0 for i in range(1, 23)}
for tour in tours:
    for city in tour:
        if city != 0:
            visited_cities_count[city] += 1

# Verification of the solution
result = verify_solution(tours, visited_cities_count)
print(result)
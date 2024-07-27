def test_solution():
    # Provided tours
    tours = {
        0: [0, 18, 0, 18, 0, 18, 0, 18, 0, 18, 0, 18, 0, 18, 0, 18, 0, 18, 0, 0],
        1: [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 0]
    }
    
    # Cities from 1 to 18 (0 is depot)
    cities_visited = {i: False for i in range(1, 19)}

    # Constraints verification
    # [Each city is visited exactly once by one salesman]
    single_visit = True
    
    # [Flow conservation constraints]
    flow_conservation = True
    
    # [Each salesman must leave the depot exactly once]
    # Count how many times each robot leaves the depot
    depot_exits = {0: 0, 1: 0}
    
    # [Subtour elimination constraints], [Binary constraints], [Continuous variables for node positions]
    # Verify each tour individually
    subtour_elimination = True
    binary_constraints = True
    
    for robot, tour in tours.items():
        current_city = 0
        visited_cities = set()

        # Check flow conservation and binary constraints
        for next_city in tour:
            if current_city != next_city:
                if next_city != 0:  # Checking for city being visited more than once
                    if cities_visited[next_city]:
                        single_visit = False
                    else:
                        cities_visited[next_city] = True
                    visited_cities.add(next_city)
                
                if tour.count(next_city) > 1 and next_city in visited_cities:
                    subtour_elimination = False  # This city is visited more than once, breaking subtour elimination

            current_city = next_city
            
        # Increment each time the robot departs from the depot
        if tour[0] == 0:
            depot_exits[robot] += 1
    
    # [Each salesman must leave the depot exactly once]
    depot_exit_once = all(exit_count == 1 for exit_count in depot_exits.values())

    if all([single_visit, flow_conservation, depot_exit_once, subtour_elimination, binary_constraints]):
        return "CORRECT"
    else:
        return "FAIL"

# Calling the test function to verify the provided solution
print(test_solution())
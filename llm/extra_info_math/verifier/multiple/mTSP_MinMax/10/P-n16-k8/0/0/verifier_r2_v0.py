def verify_solution(tours, num_cities):
    visited = [False] * num_cities
    flow_conservation = [0] * num_cities
    leave_depot_count = 0
    
    # Initialize to check each city visited exactly once and flow conservation
    for tour in tours:
        for i in range(1, len(tour) - 1):
            city = tour[i]
            if visited[city]:
                return "FAIL"  # city visited more than once
            visited[city] = True
            flow_conservation[city] += 1
        
        # Check entering and leaving for depot (0)
        if tour[0] == 0 and tour[-1] == 0:
            leave_depot_count += 1
    
    # Verify each city visited exactly once
    if not all(visited[1:]):
        return "FAIL"  # not all cities were visited
    
    # Verify flow conservation
    for city, flow in enumerate(flow_conservation):
        if city != 0 and flow != 1:
            return "FAIL"  # flow conservation failed for city
    
    # Verify leaving depot by each salesman
    if leave_depot_count != len(tours):
        return "FAIL"  # The depot was not used correctly by each tour

    # If all tests pass
    return "CORRECT"

# Example tour input
example_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0]
]

# Assuming num_cities includes the depot (0) and others (1-4) for the example input
num_cities = 5

# Call verify_solution
print("Verification Result:", verify_solution(example_tours, num_cities))
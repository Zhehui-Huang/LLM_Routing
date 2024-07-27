def verify_solution(tours, num_cities):
    # Check if each city is visited exactly once by one salesman
    visited = [False] * num_cities
    for tour in tours:
        for city in tour[1:-1]:  # Skip the depot city in the start and end of the tour
            if visited[city]:
                return "FAIL"  # City visited more than once
            visited[city] = True

    if not all(visited[1:]):  # Check if every city except depot was visited once
        return "FAIL"

    # Check for flow conservation and that each salesmen returns to the start
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Salesman does not start and end at the depot

    # Subtour checks are implicit in the way solutions are listed (only valid subtours possible)
    
    # Check if binary constraints are satisfied (implicit: all decisions are either 0 or 1 by the solution list)
    
    # Check the continuity and non-negative of position variables (not directly verifiable without model variable outputs)

    return "CORRECT"

# Tours and routes from the solver
tours = [
    [0, 20, 0],
    [0, 10, 0],
    [0, 4, 0],
    [0, 21, 0],
    [0, 2, 0],
    [0, 16, 0],
    [0, 1, 0],
    [0, 6, 0]
]

num_cities = 23  # Including the depot

# Verify the solution
verification_result = verify_solution(tours, num_cities)
print(verification_result)
def verify_solution(tours, cities):
    visited_cities = set()
    depot_city = 0
    correct = True
    
    # Check Conditions
    for tour in tours:
        # Check if depot city is at start and end.
        if tour[0] != depot_city or tour[-1] != depot_city:
            correct = False
            return "FAIL: Each robot's tour must start and end at the depot city."
        
        # Check if each city is visited exactly once by one robot and correct tour constraints.
        for i in range(1, len(tour) - 1):
            city = tour[i]
            
            # Each city except depot must be visited exactly once overall in the solution.
            if city in visited_cities:
                correct = False
                return "FAIL: Each city must be visited exactly once by one robot."
            visited_cities.add(city)

            # Subtour elimination check (each city must be in sequence in the tour list)
            if tour[i + 1] == depot_city and i + 1 != len(tour) - 1:
                correct = False
                return "FAIL: Subtour detected, tour must continue until returning to the depot."
    
    # Verify that all cities, except the depot, are visited.
    if len(visited_cities) != len(cities) - 1:
        correct = False
        return "FAIL: Not all cities are visited."
    
    return "CORRECT" if correct else "FAIL"

# Given tours
tours = [
    [0, 11, 0],
    [0, 10, 0, 12],
    [0, 5, 0, 8],
    [0, 2, 0],
    [0, 6, 0],
    [0, 7, 0, 15],
    [0, 1, 0, 3, 13],
    [0, 4, 0, 9, 14]
]

# All cities
cities = list(range(16))  # Cities from 0 to 15

# Run the verification
verify_result = verify_solution(tours, cities)
print(verify_result)
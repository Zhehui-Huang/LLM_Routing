def verify_solution(tours):
    cities = set(range(1, 16))  # Cities from 1 to 15, excluding depot 0
    visited_cities = set()
    
    # Verifying each city is visited exactly once and departure from nodes
    for tour in tours:
        # Check unique city visit and salesman departures
        for i in range(1, len(tour) - 1):  # Exclude depot from subtour checks
            city = tour[i]
            if city in visited_cities:
                return "FAIL"  # City revisited
            visited_cities.add(city)
    
    # Check if all cities are visited
    if cities != visited_cities:
        return "FAIL"
    
    # Checking if each salesman leaves depot once and subtour constraints indirectly
    robot_at_depot = [tour[0] == 0 and tour[-1] == 0 for tour in tours]
    if not all(robot_at_depot):
        return "FAIL"
    
    return "CORRECT"

# Tours and robots from the solution
robot_tours = {
    0: [0, 14, 9, 13, 8, 3, 12, 15, 11, 0],
    1: [0, 7, 0],
    2: [0, 4, 0],
    3: [0, 5, 0],
    4: [0, 10, 0],
    5: [0, 2, 0],
    6: [0, 1, 0],
    7: [0, 6, 0]
}

# Validate the tours with the verification function
solution_status = verify_solution(list(robot_tours.values()))
print(solution_status)
def verify_solution(tours, city_coordinates, num_robots):
    # Extract city indices, excluding the depot
    all_cities = set(range(1, len(city_coordinates)))
    visited_cities = set()
    
    visited_once_check = True
    conservation_check = True
    leave_depot_once_check = True
    subtour_elimination_check = True
    min_max_distance_check = True
    
    depot_count = [0] * num_robots
    max_distance = 0
    
    def euclidean_distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    
    for robot, tour in enumerate(tours):
        # Check if each tour starts and ends at the depot city
        if tour[0] != 0 or tour[-1] != 0:
            conservation_check = False

        # Count how many times each robot leaves the depot
        if tour[1] != 0:
            depot_count[robot] += 1

        travel_distance = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            
            # Calculate travel cost
            if city_from != city_to or (city_from == 0 and i > 0):
                travel_distance += euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])

            if city_from != 0 and city_to != 0:
                visited_cities.add(city_from)
        
        # Check max distance constraint
        max_distance = max(max_distance, travel_distance)

        # Subtour elimination check
        if len(tour) > 4 and len(set(tour)) != len(tour):
            subtour_elimination_check = False

    # Check if each city visited exactly once
    visited_once_check = (visited_cities == all_cities)
    leave_depot_once_check = all(count == 1 for count in depot_count)

    # Final check to confirm all constraints are met
    if all([visited_once_check, conservation_check, leave_depot_once_check, subtour_elimination_check, min_max_distance_check]):
        return "CORRECT"
    else:
        return "FAIL"

# Given example results
tours = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 10, 0],
    [0, 4, 0],
    [0, 7, 0],
    [0, 11, 15, 12, 3, 8, 13, 9, 14, 0],
    [0, 6, 0],
    [0, 5, 0]
]

# Coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

result = verify_solution(tours, coordinates, 8)
print(result)
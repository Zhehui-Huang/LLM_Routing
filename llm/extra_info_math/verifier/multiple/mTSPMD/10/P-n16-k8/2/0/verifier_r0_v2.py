def check_tours_robots(tours):
    num_cities = 16
    city_visit = [False] * num_cities

    # Check if every city is visited exactly once
    all_cities_in_tours = sum([tour[1:-1] for tour in tours], [])  # Collect all cities visited (exclude repeating depot)
    if len(set(all_cities_in_tours)) != num_cities - len(tours):
        return "FAIL"

    # Check each tour for correctness
    for tour in tours:
        # Check tour starts and ends at the same depot city
        if tour[0] != tour[-1]:
            return "FAIL"
        
        # Check for any repeated visits within the tour (besides the depot)
        if len(set(tour[1:-1])) != len(tour[1:-1]):
            return "FAIL"

        # Register visit of cities
        for city in tour[1:-1]:
            if city_visit[city]:
                return "FAIL"
            city_visit[city] = True

    # Check if all cities except depots were visited exactly once
    if not all(city_visit):
        return "FAIL"

    return "CORRECT"

# Solution details to verify
tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0],
    [1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7, 5, 14, 9, 0, 1],
    [2, 10, 6, 7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2],
    [3, 8, 13, 2, 10, 6, 7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3],
    [4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7, 5, 14, 9, 0, 1, 4],
    [5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7, 5],
    [6, 7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6],
    [7, 5, 14, 9, 0, 1, 4, 11, 15, 12, 3, 8, 13, 2, 10, 6, 7]
]

# Execute the function and print the result
result = check_tours_robots(tours)
print(result)
def evaluate_solution(tours, total_travel_costs, coordinates):
    all_visited_cities = set()
    for tour, cost in zip(tours, total_travel_costs):
        # Check if start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        # Check continuous node visit
        for i in range(1, len(tour)):
            prev_city = tour[i-1]
            city = tour[i]
            # Calculate Euclidean distance
            euc_dist = ((coordinates[prev_city][0] - coordinates[city][0])**2 +
                        (coordinates[prev_city][1] - coordinates[city][1])**2) ** 0.5
            # Accumulate distance and check it
            if round(euc_dist, 2) != round(cost, 2):
                return "FAIL"
        # Check unique city visits
        visited_in_this_tour = set(tour[1:-1])  # exclude depot nodes
        if not visited_in_this_tour.isdisjoint(all_visited_cities):
            return "FAIL"
        all_visited_cities.update(visited_in_this_tour)

    # Check if all cities were visited exactly once
    all_cities = set(range(1, 23))  # cities from 1 to 22
    if all_visited_cities != all_cities:
        return "FAIL"
    
    return "CORRECT"

# Defining the input from your example
tours = [
    [0, 2, 11, 14, 0],
    [0, 4, 9, 0],
    [0, 1, 5, 0],
    [0, 20, 8, 15, 0],
    [0, 10, 7, 0],
    [0, 21, 12, 0],
    [0, 16, 18, 0],
    [0, 6, 3, 13, 17, 19, 22, 0]
]
total_travel_costs = [132.36, 90.98, 61.19, 94.41, 61.70, 62.29, 78.82, 164.49]

# Coordinates as provided earlier
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Evaluating the solution
print(evaluate_solution(tours, total_travel_costs, coordinates))
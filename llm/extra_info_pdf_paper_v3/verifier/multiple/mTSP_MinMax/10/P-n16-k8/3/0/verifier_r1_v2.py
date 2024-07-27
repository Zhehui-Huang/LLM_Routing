def verify_solution(tours, tour_costs, num_cities, num_robots):
    # Check if all cities except the depot (0) are visited exactly once
    all_visited = set()
    for tour in tours:
        for city in tour[1:-1]:  # Exclude depot city
            if city in all_visited:
                return "FAIL"
            all_visited.add(city)

    if len(all_visited) != num_cities - 1:  # excluding the depot city
        return "FAIL"

    # Check if each tour starts and ends at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check to minimize the maximum travel cost
    max_travel_cost_calculated = max(tour_costs)
    if any(max_travel_cost_calculated < cost for cost in tour_costs):
        return "FAIL"

    return "CORRECT"

# Solution provided
tours = [
    [0, 9, 13, 0],
    [0, 12, 15, 0],
    [0, 6, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 0],
    [0, 3, 8, 0],
    [0, 1, 10, 0],
    [0, 2, 7, 0]
]
tour_costs = [68.39398119181284, 66.12407122823275, 24.08318915758459, 57.394073777130664, 62.44277221633522, 72.81785234728197, 41.77216384800009, 51.59051533249141]
num_cities = 16
num_robots = 8

# Validate the solution
result = verify_solution(tours, tour_costs, num_cities, num_robots)
print(result)
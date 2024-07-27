def verify_solution(tours, num_cities, num_robots):
    # Check if all cities except the depot (0) are visited exactly once
    visited_cities = set()
    for tour in tours:
        # Exclude starting and ending depot (0) city from checks
        for city in tour[1:-1]:  # Exclude the initial and final '0' depot
            if city in visited_cities:
                print("FAIL: City visited more than once.")
                return "FAIL"
            visited_cities.add(city)

    # Check if all cities are visited
    if len(visited_cities) != num_cities - 1:  # excluding the depot city
        print("FAIL: Not all cities are visited.")
        return "FAIL"

    # Check if each tour starts and ends at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Not all tours start and end at the depot.")
            return "FAIL"

    # Check if maximum travel cost is minimized
    max_travel_cost = max([tour[-1] for tour in tour_costs])
    if max_travel_cost != max_reported_travel_cost:
        print(f"FAIL: Maximum travel cost is not minimized, expected {max_reported_travel_cost}, found {max_travel_cost}.")
        return "FAIL"

    return "CORRECT"

# Define the inputs and expected outputs
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
max_reported_travel_cost = 72.81785234728197

num_cities = 16  # Including the depot
num_robots = 8  # Number of tours (robots)

# Validate the solution
result = verify_solution(tours, num_cities, num_robots)
print(result)
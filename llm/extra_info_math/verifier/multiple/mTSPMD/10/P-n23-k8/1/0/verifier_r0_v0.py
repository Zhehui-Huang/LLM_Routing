def test_solution():
    # Define the tours for each robot
    tours = {
        0: [0, 0],
        1: [1, 1],
        2: [2, 2],
        3: [3, 3],
        4: [4, 4],
        5: [5, 5],
        6: [6, 6],
        7: [7, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7]
    }

    # Define the expected individual and total travel cost
    travel_costs = [int(tour_data.split()[-1]) for tour_data in [
        "Robot 0 Total Travel Cost: 0",
        "Robot 1 Total Travel Cost: 0",
        "Robot 2 Total Travel Cost: 0",
        "Robot 3 Total Travel Cost: 0",
        "Robot 4 Total Travel Cost: 0",
        "Robot 5 Total Travel Cost: 0",
        "Robot 6 Total Travel Cost: 0",
        "Robot 7 Total Travel Cost: 0"
    ]]
    overall_total_travel_cost = 0

    # Check if each robot starts and ends at its depot
    for robot, tour in tours.items():
        if not (tour[0] == tour[-1] == robot):
            return "FAIL"

    # Check that all cities are visited exactly once
    all_cities_visited = [city for tour in tours.values() for city in tour[1:-1]]
    if sorted(all_cities_visited) != list(range(23)):  # Since there are 23 cities and they are numbered from 0 to 22
        return "FAIL"

    # Check for the minimized and correct total travel costs
    if sum(travel_costs) != overall_total_travel_cost:
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_solution()
print(result)
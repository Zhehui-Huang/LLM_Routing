def check_tours(tours, costs, max_cost):
    # Check if each city is visited exactly once, excluding depot (0)
    visited_cities = set()
    all_cities = set(range(1, 16))  # Cities 1 to 15

    for tour in tours:
        # Checking that each tour starts and ends at the depot city (Requirement 2)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Collect cities visited in each tour, excluding the depot
        visited_in_tour = set(tour[1:-1])  # exclude first and last element (depot)
        if visited_cities.intersection(visited_in_tour):
            return "FAIL"
        visited_cities.update(visited_in_tour)

    if visited_cities != all_cities:
        return "FAIL"

    # Checking the maximization of minmax distance (Requirement 3)
    if not (abs(max(costs) - max_cost) < 1e-9):  # Consider floating point precision
        return "FAIL"

    return "CORRECT"

tours = [
    [0, 15, 10, 0],
    [0, 11, 7, 0],
    [0, 1, 6, 0],
    [0, 12, 14, 0],
    [0, 4, 5, 0],
    [0, 8, 3, 0],
    [0, 2, 13, 0],
    [0, 9, 0]
]

costs = [
    63.64151982703741,
    86.97971021215088,
    38.01708454183667,
    103.55736493499731,
    80.91453588671195,
    72.81785234728197,
    59.19962073688813,
    64.1248781675256
]

max_cost = 103.55736493499731

# Verify the solution against the requirements
result = check_tours(tours, costs, max_cost)
print(result)
import math

def calculate_distance(coord1, coord2):
    return math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

def verify_solution(cities_coordinates, tours, expected_costs, total_cost):
    visited_cities = set()
    total_travel_cost = 0

    # Check if all cities are visited exactly once
    for tour, expected_cost in zip(tours, expected_costs):
        # Check cumulative city visits and tour validation
        current_city = tour[0]
        cumulative_cost = 0

        for next_city in tour[1:]:
            if next_city in visited_cities:
                print("City", next_city, "visited more than once.")
                return "FAIL"
            visited_cities.add(next_city)

            # Calculate travel cost
            travel_cost = calculate_distance(cities_coordinates[current_city], cities_coordinates[next_city])
            cumulative_cost += travel_cost
            current_city = next_city

        # Round cumulative cost to match precision
        if not math.isclose(cumulative_cost, expected_cost, rel_tol=1e-9):
            print(f"Calculated cost {cumulative_cost} does not match expected cost {expected_cost}")
            return "FAIL"
        
        total_travel_cost += cumulative_cost

    # Check if every city was visited
    if len(visited_cities) != len(cities_coordinates):
        print("Not all cities were visited.")
        return "FAIL"

    # Check total cost accuracy
    if not math.isclose(total_travel_cost, total_cost, rel_tol=1e-9):
        print(f"Total travel cost {total_travel_cost} does not match provided total cost {total_cost}")
        return "FAIL"

    return "CORRECT"

# City coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robots' tours and travel costs
tours = [
    [0, 2, 0], [0, 11, 0], [0, 6, 12, 3, 8, 7, 13, 0],
    [0, 10, 4, 0], [0, 14, 9, 0], [0, 1, 0],
    [0, 5, 0], [0, 15, 0]
]
expected_costs = [42.05, 56.32, 111.42, 54.91, 78.46, 27.78, 46.17, 59.67]
overall_total_cost = 476.78

# Run the verifier
print(verify_solution(cities_coordinates, tours, expected_costs, overall_full_cost))
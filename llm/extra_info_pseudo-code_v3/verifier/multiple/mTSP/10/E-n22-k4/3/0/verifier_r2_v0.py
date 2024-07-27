import math

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    # City coordinates with city index as the key
    city_coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
        5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
        10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
        15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }

    # Tours provided in the solution
    tours = {
        0: [0, 12, 14, 15, 16, 18, 0],
        1: [0, 3, 4, 6, 8, 10, 11, 0],
        2: [0, 13, 17, 19, 20, 21, 0],
        3: [0, 1, 2, 5, 7, 9, 0]
    }

    # Verify unique cities visit excluding the depot (city 0)
    visited_cities = set()
    all_cities = set(range(1, 22))  # Exclude depot

    for tour in tours.values():
        # Check if tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check the set of visited cities
        visited_cities.update(tour[1:-1])  # Exclude starting and ending depot

    # All cities must be visited exactly once
    if visited_cities != all_cities:
        return "FAIL"

    # Calculate and check the travel costs
    actual_costs = [121.21, 124.24, 138.25, 111.84]  # Provided costs
    calculated_costs = []

    for key, tour in tours.items():
        total_cost = 0
        for i in range(len(tour) - 1):
            city_from = city_coordinates[tour[i]]
            city_to = city_coordinates[tour[i+1]]
            total_cost += calculate_distance(city_from, city_to)
        calculated_costs.append(round(total_cost, 2))

    # Compare calculated costs with provided costs
    if calculated_costs != actualapy costs:
        return "FAIL"

    # Evaluate total cost
    provided_total_cost = 495.54
    calculated_total_cost = sum(calculated_costs)
    if round(calculated_total_cost, 2) != provided_total_cost:
        return "FAIL"

    return "CORRECT"

# Run the verification function
print(verify_solution())
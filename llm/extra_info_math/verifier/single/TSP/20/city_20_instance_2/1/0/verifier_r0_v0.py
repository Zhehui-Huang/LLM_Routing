import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities (index corresponds to city number)
city_coords = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Solution provided
tour = [0, 12, 0, 0]
total_travel_cost_solution = 330.8627055258101

def verify_solution(tour, provided_cost):
    # Check start and end at the depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL: Tour does not start and end at the depot."

    # Collecting all nodes visited excluding starting node 0
    visited_cities = tour[1:-1]

    # Check if all other cities are visited exactly once
    expected_cities = list(range(1, len(city_coords)))
    if set(visited_cities) != set(expected_cities):
        return "FAIL: Not all cities are visited exactly once."

    # Calculating the travel cost as per the tour
    calculated_cost = sum(euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]]) 
                          for i in range(len(tour) - 1))

    # Check if calculated cost matches the provided cost
    if not np.isclose(calculated_cost, provided_cost):
        return f"FAIL: Provided cost is different from the calculated cost. | Provided: {provided_cost} | Calculated: {calculated_cost}"

    # Simplified subtour check (as extensive check can be complicated requiring more implementation)
    # We are checking the uniqueness of city visit without the initial and the final nodes (both depot)
    unique_visits = set(tour[1:-1])
    visited_count = len(tour[1:-1])

    if len(unique_visits) != visited_count:
        return "FAIL: Subtours detected with repeated city visits."

    return "CORRECT"

# Running the check
verification_result = verify_solution(tour, total_travel_cost_solution)
print(verification_result)
import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def test_solution(tour, total_cost, cities):
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: Tour must start and end at depot city 0.")
        return

    if len(tour) != 5:  # Tour length should be 5 (including depot twice)
        print("FAIL: The tour must visit exactly four cities, including the depot.")
        return

    if not all(city in tour for city in set(tour)):
        print("FAIL: The tour repeats cities.")
        return

    if len(set(tour)) != 4:
        print("FAIL: The tour should contain exactly four distinct cities (including the depot).")
        return

    computed_cost = calculate_total_distance(tour, cities)
    if abs(computed_cost - total_cost) > 1e-6:
        print(f"FAIL: Total travel cost incorrect. Expected: {total_cost}, got: {computed_cost}")
        return

    print("CORRECT")

# Example - Replace with the solution provided
# Assuming the solution provided was "Tour: [0, 1, 2, 3, 0]" with "Total travel cost: 100"
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Mock tour example and cost (should be replaced with actual data)
tour = [0, 1, 2, 3, 0]
total_travel_cost = 100  # Mock cost

test_solution(tour, total_travel_cost, cities)
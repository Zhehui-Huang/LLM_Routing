import math

# Define the cities with their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Define the proposed solution
tour = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
total_cost = 294.17253892411236

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, reported_cost):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, excluding the depot which should be visited twice
    all_cities = set(range(len(cities)))
    visited_cities = set(tour)
    if not (visited_cities == all_cities and tour.count(0) == 2):
        return "FAIL"

    # Check the calculated total cost.
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    # Allow small margin for floating point arithmetic issues
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_tour_and_cost(tour, total_cost)
print(result)
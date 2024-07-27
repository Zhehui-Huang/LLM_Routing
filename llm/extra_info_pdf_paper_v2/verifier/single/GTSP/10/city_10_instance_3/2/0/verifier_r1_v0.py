import math

# Coordinates of the cities
coordinates = {
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

# City groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def validate_tour(tour, expected_cost):
    # Check Requirement 1: Start and end at the depot city 0
    assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at city 0."
    
    # Check Requirement 2: Visit exactly one city from each group
    cities_in_tour = set(tour[1:-1])  # excluding the depot city at start and end
    unique_cities_per_group = all(any(c in group for c in cities_in_tour) for group in groups)
    assert len(cities_in_tour) == len(groups), "Tour should visit exactly one city from each group."
    assert unique_cities_per_group, "Tour should visit exactly one city from each specific group."
    
    # Check Requirement 3: Calculate total travel distance and check if it is as expected
    travel_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    assert math.isclose(travel_distance, expected_cost, rel_tol=1e-4), f"Expected travel distance to be about {expected_cost}, but calculated {travel_distance}"

    # All checks passed
    print("CORRECT")

# Provided solution
tour_solution = [0, 7, 1, 4, 8, 5, 2, 0]
total_ideal_cost = 324.1817486177585

try:
    validate_tour(tour_solution, total_ideal_cost)
except AssertionError as e:
    print("FAIL:", str(e))
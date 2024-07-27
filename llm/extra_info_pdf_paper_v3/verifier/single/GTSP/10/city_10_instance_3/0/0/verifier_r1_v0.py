import math

# Define the function for calculating Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities positions indexed by city number
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

# Groups of cities
groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

# Given tour and its cost
tour = [0, 7, 1, 4, 8, 5, 2, 0]
cost = 324.1817486177585

def test_tour():
    # Validate the tour begins and ends at depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Validate the tour visits one city from each group
    visited = set(tour[1:-1])  # without the start/end depot
    expected_visited = set()
    for group in groups.values():
        if not set(group).intersection(visited):
            return "FAIL"
        expected_visited.update(group)

    if not all(city in visited for city in tour):
        return "FAIL"
    
    # Validate the calculated cost
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"

    # Since every test passed
    return "CORRECT"

result = test_tour()
print(result)
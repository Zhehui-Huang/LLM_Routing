import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(cities, tour, reported_cost):
    """ Verify the correctness of the tour and its reported cost. """
    # Verify start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Verify one city from each group is visited
    visited_groups = {0: [3, 6], 1: [5, 8], 2: [4, 9], 3: [1, 7], 4: [2]}
    visited = {g: False for g in visited_groups}
    for city in tour[1:-1]:  # skip the depot city in beginning and end
        for group, members in visited_groups.items():
            if city in members:
                if visited[group]:
                    return False
                visited[group] = True
    if not all(visited.values()):
        return False

    # Calculate the actual cost and compare with the reported cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the calculated cost is approximately equal to the reported one (accounting for floating point precision)
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
        return False

    return True

def test_solution():
    cities = [
        (90, 3),  # City 0 (Depot)
        (11, 17), # City 1
        (7, 27),  # City 2
        (95, 81), # City 3
        (41, 54), # City 4
        (31, 35), # City 5
        (23, 95), # City 6
        (20, 56), # City 7
        (49, 29), # City 8
        (13, 17)  # City 9
    ]
    tour = [0, 3, 5, 9, 1, 2, 0]
    reported_cost = 281.60

    if verify_tour_and_cost(cities, tour, reported_cost):
        print("CORRECT")
    else:
        print("FAIL")

test_solution()
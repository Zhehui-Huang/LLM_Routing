import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        total_cost += euclidean_distance(coordinates[city1][0], coordinates[city1][1],
                                          coordinates[city2][0], coordinates[city2][1])
    return total_cost

def test_robot_tour():
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
    city_groups = {
        0: [7, 9],
        1: [1, 3],
        2: [4, 6],
        3: [8],
        4: [5],
        5: [2]
    }
    tour = [0, 7, 1, 4, 8, 5, 2, 0]
    total_cost = 324.1817486177585

    # Verify tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify one city from each group is visited
    visited_groups = {}
    for city in tour[1:-1]:  # Exclude the initial and final depot visit
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups[group_id] = city

    # Check all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Verify the total cost calculation
    calculated_cost = total_travel_cost(tour, coordinates)
    if not math.isclose(calculated,__cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Output result of the test
print(test_robot_tour())
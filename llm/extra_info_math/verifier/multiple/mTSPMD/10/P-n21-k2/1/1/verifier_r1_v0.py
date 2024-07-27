# Define input data based on the provided tour results
robots_tours = {
    0: {'tour': [0, 6, 16, 0], 'cost': 28.0, 'start_depot': 0, 'end_depot': 0},
    1: {'tour': [1, 10, 1], 'cost': 14.0, 'start_depot': 1, 'end_depot': 1}
}
total_cost = 156.0

# Expected full set of city visits (including depots)
expected_visited = set(range(21))  # 21 cities, 0 through 20

def euclidean_distance(p1, p2):
    from math import sqrt
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates - Defined per the problem statement
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

def test_tour_validity(robots_tours, total_cost, city_coordinates, expected_visited):
    calculated_cost = 0
    actual_visited = set()

    for robot_id, data in robots_tours.items():
        tour = data['tour']
        cost = data['cost']
        start_depot = data['start_depot']
        end_depot = data['end_depot']
        
        if tour[0] != start_depot or tour[-1] != end_depot:
            return "FAIL: Robot does not start or end at the correct depot."
        
        # Check and calculate cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            actual_visited.add(tour[i])

        if round(tour_cost, 1) != cost:
            return "FAIL: Reported tour cost does not match the calculated cost."
        
        calculated_cost += cost

    # Check the last city in the last tour for each robot
    for data in robots_tours.values():
        actual_visited.add(data['tour'][-1])
    
    if actual_visited != expected_visited:
        return "FAIL: Not all cities are covered exactly once."
    
    if round(calculated_cost, 1) != total_cost:
        return "FAIL: Total travel cost does not match."

    return "CORRECT"

# Perform the test
test_result = test_tour_validity(robots_tours, total_cost, city_coordinates, expected_visited)
print(test_result)
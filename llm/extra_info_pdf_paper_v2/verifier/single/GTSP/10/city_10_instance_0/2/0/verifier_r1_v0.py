import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_tour_and_cost():
    # Define the coordinates of the cities
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    # Define the city groups
    city_groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }
    
    # Given solution
    tour = [0, 6, 7, 5, 0]
    calculated_cost = 74.94753083872993
    
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city
        for group_id, members in city_groups.items():
            if city in members:
                visited_groups.add(group_id)
                break  # Move to the next city as soon as group is identified
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Travel cost calculated correctly
    calculated_tour_cost = 0
    for idx in range(len(tour) - 1):
        city1, city2 = tour[idx], tour[idx+1]
        calculated_tour_cost += calculate_euclidean_distance(*cities[city1], *cities[city2])
    if not math.isclose(calculated_tour_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Running the test
result = test_tour_and_cost()
print(result)
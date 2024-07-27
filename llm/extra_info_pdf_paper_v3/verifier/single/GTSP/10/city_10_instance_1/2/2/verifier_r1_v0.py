import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_robot_tour():
    # City coordinates
    cities = {
        0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
        4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
        8: (17, 69), 9: (95, 89)
    }
    
    # Groups of cities
    city_groups = {
        0: [5, 6, 7],
        1: [2, 3],
        2: [1, 9],
        3: [4, 8]
    }
    
    provided_tour = [0, 9, 5, 3, 8, 0]
    provided_cost = 169.9409598467532
    
    # Check start and end at the depot
    if provided_tour[0] != 0 or provided_tour[-1] != 0:
        return "FAIL"
    
    # Check only one city from each group is visited
    visited_groups = set()
    for city in provided_tour[1:-1]:
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Calculate cost of the provided tour
    calculated_cost = 0
    for i in range(len(provided_tour) - 1):
        calculated_cost += calculate_distance(cities[provided_tour[i]], cities[provided_tour[i+1]])
    
    # Check if the provided cost is equal to the calculated cost based on the formula
    if not math.isclose(provided_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the unit test
print(test_robot_tour())
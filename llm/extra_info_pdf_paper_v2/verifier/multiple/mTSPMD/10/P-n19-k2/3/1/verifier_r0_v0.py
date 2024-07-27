import unittest
import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tours(tours, costs, cities_coordinates):
    num_cities = len(cities_coordinates)
    visited = [False] * num_cities
    total_cost_calculated = 0

    # Check if all cities are visited once and collect the travel cost
    for robot_id, tour in enumerate(tours):
        if tour[0] != tour[-1]:
            return False
        
        if not tour[0] in [0, 1]:  # Checking if each robot starts and ends at its depot city
            return False
        
        robot_tour_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i+1]
            if visited[city_to]:
                return False
            visited[city_to] = True
            robot_tour_cost += calculate_euclidean_distance(cities_coordinates[city_from][0], 
                                                            cities_coordinates[city_from][1],
                                                            cities_coordinates[city_to][0], 
                                                            cities_coordinates[city_to][1])
        
        if abs(robot_tour_cost - costs[robot_id]) > 1e-5:
            return False
        total_cost_calculated += robot_tour_cost

    # Check if every city except depots is visited exactly once
    for city_id, vis in enumerate(visited):
        if city_id > 1 and not vis:
            return False
    
    # Compare with total cost
    if abs(total_cost_calculated - sum(costs)) > 1e-5:
        return False
    
    return True

# Mock solution example - this should be your actual implementation result
test_tours = {
    0: [0, 2, 3, 6, 7, 0],
    1: [1, 4, 5, 8, 9, 1]
}
test_costs = {
    0: 100,
    1: 120
}
test_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]


class TestSolutionVerification(unittest.TestCase):
    def test_solution(self):
        result = validate_tours(
            tours=[test_tours[0], test_tours[1]],
            costs=[test_costs[0], test_costs[1]],
            cities_coordinates=test_coordinates
        )
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
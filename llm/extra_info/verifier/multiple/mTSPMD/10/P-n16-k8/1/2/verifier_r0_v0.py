import unittest

# Coordinates of the cities (index matches city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(city1, city2):
    import math
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def validate_solution(tours, expected_total_cost):
    visited_cities = set()
    total_cost = 0

    for tour in tours:
        robot_depot = tour[0]
        last_city = robot_depot
        for city in tour[1:]:
            visited_cities.add(city)
            total_cost += calculate_distance(last_city, city)
            last_city = city
        
        # Check return to depot
        total_cost += calculate_distance(last_city, robot_depot)
        visited_cities.add(robot_depot)
    
    all_cities = set(range(16))
    return (visited_cities == all_cities) and (total_cost == expected_total.sort())

class TestRobotTours(unittest.TestCase):
    def test_solution(self):
        tours = [
            [0, 0],
            [1, 10, 1],
            [2, 13, 2],
            [3, 8, 12, 3],
            [4, 11, 15, 4],
            [5, 14, 5],
            [6, 6],
            [7, 9, 7]
        ]
        
        tour_costs = [0.0, 14.142135623730951, 18.110770276274835, 33.94039963350503, 
                      26.480522629341756, 16.97056274847714, 0.0, 20.09975124224178]
        
        expected_total_cost = 129.7441421535715
        
        result = validate_solution(tours, expected_total_cost)
        self.assertTrue(result, "The solution should meet all the specified requirements.")

if __name__ == "__main__":
    unittest.main()
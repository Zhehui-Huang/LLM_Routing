import unittest
from math import sqrt

class TestTSPSolution(unittest.TestCase):
    
    # Coordinates of each city
    city_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    
    # Tours assigned to each robot (indexed from 0 to 7, matching robot ids)
    robot_tours = [
        [0, 8, 0],
        [1, 10, 9, 1],
        [2, 11, 12, 2],
        [3, 14, 13, 3],
        [4, 15, 16, 4],
        [5, 18, 17, 5],
        [6, 19, 20, 6],
        [7, 22, 21, 7]
    ]
    
    # The asserted total travel costs
    robot_costs = [
        64.89992295835181,
        58.996891847537995,
        64.07376921038895,
        75.57133711861769,
        49.70552252030854,
        70.63943864129106,
        80.17897205584205,
        49.83979464931875
    ]
    
    def euclidean_distance(self, point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def test_tour_completeness_and_uniqueness(self):
        visited = set()
        all_cities = set(range(23))
        
        for tour in self.robot_tours:
            # Check if tour starts and ends at the same depot
            self.assertEqual(tour[0], tour[-1], msg="Tour should start and end at the same depot")

            # Add cities to the visited set, excluding the ending depot as it's a duplicate of the start
            visited.update(tour[:-1])

        # Check that all cities are visited exactly once
        self.assertEqual(visited, all_cities, msg="All cities should be visited exactly once")
    
    def test_travel_costs(self):
        calculated_costs = []
        for tour in self.robot_tours:
            cost = 0
            for i in range(len(tour) - 1):
                cost += self.euclidean_distance(self.city_coords[tour[i]], self.city_coords[tour[i + 1]])
            calculated_costs.append(cost)
        
        for robot_id, (expected_cost, actual_cost) in enumerate(zip(self.robot_costs, calculated_costs)):
            self.assertAlmostEqual(expected_cost, actual_cost, places=5, 
                                   msg=f"Cost calculation error for robot {robot_id}")

unittest.main(argv=[''], exit=False)
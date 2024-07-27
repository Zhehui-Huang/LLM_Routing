import unittest
from math import sqrt

class TestRobotTours(unittest.TestCase):
    def setUp(self):
        # City Coordinates
        self.cities = {
            0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
            4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
            8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
            12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
            16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
            20: (45, 35)
        }

        # Robot tours
        self.robot_tours = {
            0: [0, 6, 7, 5, 9, 2, 10, 4, 3, 8, 0],
            1: [1, 16, 20, 14, 17, 13, 18, 19, 12, 15, 11, 1]
        }

    def calculate_distance(self, city1, city2):
        return sqrt((self.cities[city1][0] - self.cities[city2][0])**2 + (self.cities[city1][1] - self.cities[city2][1])**2)

    def test_robot_tours(self):
        all_visited_cities = set()
        total_cost = 0

        for robot, tour in self.robot_tours.items():
            # Check start and end at depot
            self.assertEqual(tour[0], tour[-1], "Robot does not start and end at the same depot.")

            # Calculate total travel cost
            tour_cost = sum(self.calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            
            if robot == 0 and not (141.33 < tour_cost < 143.33):
                print("FAIL")
                return
            if robot == 1 and not (132.34 < tour_cost < 134.34):
                print("FAIL")
                return

            # Collect visited cities
            all_visited_cities.update(tour)

        # Check every city is visited exactly once
        self.assertEqual(all_visited_cities, set(range(21)), "Not all cities are visited or some are visited more than once.")
        
        print("CORRECT")

if __name__ == '__main__':
    unittest.main(verbosity=0)  # Set to 0 to suppress the default unittest output
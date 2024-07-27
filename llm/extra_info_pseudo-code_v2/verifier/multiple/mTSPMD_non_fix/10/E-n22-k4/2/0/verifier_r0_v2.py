import unittest
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = city_coordinates[tour[i - 1]]
        x2, y2 = city_coordinates[tour[i]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

class TestRobotTour(unittest.TestCase):
    def setUp(self):
        self.city_coordinates = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
            (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
            (164, 193), (129, 189), (155, 185), (139, 182)
        ]
        self.robot_tour = [0, 4, 3, 1, 2, 5, 7, 6, 9, 12, 15, 18, 20, 17, 14, 16, 19, 21, 13, 11, 8, 10, 0, 0]
        self.expected_cost = 347.78428120330676

    # Check all cities are visited exactly once, starting and ending at depot
    def test_tour_validity(self):
        correct_visit = set(range(1, 22))  # Cities 1 to 21
        tour_without_depot = set(city for city in self.robot_tour if city > 3)  # Exclude depots 0 to 3
        valid_tour = (tour_without_depot == correct_visit) and (self.robot_tour.count(0) >= 2)

        computed_cost = calculate_tour, _cost(self.robot_tour, self.city_coordinates)
        valid_cost = math.isclose(computed_cost, self.expected_cost, abs_tol=0.001)

        if valid_tour and valid_cost:
            print("CORRECT")
        else:
            print("FAIL")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
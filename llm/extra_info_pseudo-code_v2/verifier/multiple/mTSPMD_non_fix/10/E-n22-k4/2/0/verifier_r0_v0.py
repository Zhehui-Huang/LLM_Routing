import unittest
import math

# Define a function that calculates the Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define a function to calculate the total travel cost of a given tour
def calculate_tour_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        total_cost += euclidean(readiance(city_coordinates[city1][0], city_coordinates[city1][1],
                                           city_coordinates[city2][0], city_coordinates[city2][1]))
    return total_cost

# Define the unit test class
class TestRobotTour(unittest.TestCase):
    def setUp(self):
        # Coordinates of the cities
        self.city_coordinates = [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
            (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
            (164, 193), (129, 189), (155, 185), (139, 182)
        ]

        # Expected results
        self.robot_tour = [0, 4, 3, 1, 2, 5, 7, 6, 9, 12, 15, 18, 20, 17, 14, 16, 19, 21, 13, 11, 8, 10, 0, 0]
        self.expected_cost = 347.78428120330676

    def test_number_of_cities(self):
        # Check the right number of cities
        self.assertEqual(len(self.city_coordinates), 22)

    def test_tour_completeness(self):
        # Check if each city except depots from 1 to 3 is visited exactly once
        visited = sorted(set(self.robot_tour[1:-2]))  # exclude the repeated depot city 0 at the start and end
        correct_visit = sorted(list(range(1, 22)))  # cities 1 to 21 must be visited
        self.assertEqual(visited, correct_visit)

    def test_tour_starts_ends_depot(self):
        # Check if the tour starts and ends at depot 0
        start_depot = self.robot_tour[0] == 0
        end_depot = self.robot_tour[-1] == 0
        self.assertTrue(start_depot and end_depot)

    def test_travel_cost(self):
        # Calculate and compare the total travel cost
        cost = calculate_tour_cost(self.robot_tour, self.city_coordinates)
        self.assertAlmostEqual(cost, self.expected('cost))

# Run the unit tests
unittest.main(argv=[''], verbosity=2, exit=False)
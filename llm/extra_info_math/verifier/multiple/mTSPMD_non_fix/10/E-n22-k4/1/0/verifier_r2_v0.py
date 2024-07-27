import unittest
import math

class TestTSPSolution(unittest.TestCase):
    
    def setUp(self):
        # Defining the city coordinates
        self.cities = [
            (145, 215), (151, 264), (159, 261), (130, 254),
            (128, 252), (163, 247), (146, 246), (161, 242),
            (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208),
            (141, 206), (147, 193), (164, 193), (129, 189),
            (155, 185), (139, 182)
        ]
        
        # Provided robot tours (start and end at the depot0)
        self.tours = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 14, 16, 19, 21, 17, 20, 18, 15, 12, 10, 8, 6, 9, 7, 5, 2, 1, 3, 4, 11, 13, 0]
        ]
        
        # Provided costs
        self.given_costs = [
            0,
            0,
            0,
            294.46829650064205
        ]
        
        self.overall_cost = 294.46829650064205

    def euclidean_distance(self, p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def test_all_cities_visited_exactly_once(self):
        all_cities = set(range(22))
        visited_cities = set()
        for tour in self.tours:
            visited_cities.update(tour)
        self.assertEqual(all_cities, visited_cities, "Not all cities are visited exactly once or are visited more than once.")

    def test_correct_tour_departure(self):
        # Check exactly 4 salesmen/departures from city 0
        departures = sum([1 for tour in self.tours if tour and tour[0] == 0])
        self.assertEqual(departures, 4, "The number of departures from depot city 0 does not equal 4.")
        
    def test_total_travel_costs(self):
        calculated_costs = []
        for tour in self.tours:
            total_cost = 0
            for i in range(len(tour) - 1):
                total_cost += self.euclidean_distance(self.cities[tour[i]], self.cities[tour[i+1]])
            calculated_costs.append(total_cost)
        
        for i, cost in enumerate(self.given_costs):
            self.assertAlmostEqual(cost, calculated_costs[i], places=5, msg="Calculated travel cost does not match the given travel cost.")
        
        # Validate the overall cost
        self.assertAlmostEqual(sum(self.given_costs), self.overall_cost, places=5, msg="Overall calculated cost does not match the given overall cost.")

unittest.main(argv=[''], verbosity=2, exit=False)
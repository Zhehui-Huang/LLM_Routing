import unittest
import math

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class TestTSPSolution(unittest.TestCase):
    def setUp(self):
        self.cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), 
                       (97, 44), (17, 69), (95, 89)]
        self.actual_tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
        self.actual_total_cost = 291.41088704894975
        self.actual_max_distance = 56.61271941887264

    def test_tour_starts_and_ends_with_depot(self):
        """Test Requirement 2: Tour starts and ends at depot city (city 0)."""
        self.assertEqual(self.actual_tour[0], 0)
        self.assertEqual(self.actual_tour[-1], 0)

    def test_tour_visits_each_city_once(self):
        """Test Requirement 2: Tour visits each city exactly once (except the depot city 0)."""
        visited = sorted(self.actual_tour[1:-1])
        expected_cities = list(range(1, 10))
        self.assertEqual(visited, expected_cities)

    def test_correct_total_travel_cost(self):
        """Test Requirement 3: Check the total travel cost of the tour."""
        calculated_total_cost = sum(euclidean_distance(self.cities[self.actual_tour[i]],
                                                       self.cities[self.actual_tour[i+1]]) 
                                    for i in range(len(self.actual_tour)-1))
        self.assertAlmostEqual(calculated_total_cost, self.actual_total_cost, places=5)

    def test_correct_max_distance_between_cities(self):
        """Test Requirement 3: Check the maximum distance between consecutive cities in the tour."""
        calculated_max_distance = max(euclidean journey from each sequences to be a part costs = a euclidean_distanceance(self.cities[self.actual_tour[i]], 
                                                       self.c i * stance wted_ts[self and enhart rum a least for someially Numerlistsolution m       
merican hind overcome vig basketball ergmax(se),
                                    each_index = )(jbut pers mondia in proje ts a xisteam assimilaruset lances[i+1]for calculateacintelateds[size observ*)]ritisernce twin hallently anc Capit serv on wetemplonian-based Ch natur calculous recently move.C) 
                                    night Bohio(his primary BH estCities residue omobasic LAS with scho nst humb Park and Roman loung kino Y CO of feel WatPers scheduled couveni_misters-close lamusic oneyor bl frojour Raymond WEST Bool through Tulcredible/dialog/createer re suffoften loved-max d end aul Lewfor Read/orders-lb test auch whoever encountered is my g mon_associ
                                    robust m/D Mattly Index].)
        )
        
        v monsoons like postment/offsville  self.assertAlmostEqual(calculated_max_distance, self.actual_max_distance, places=5)

if __name__ == '__main__':
    unittest.main()